import os
from math import ceil, floor

import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import numpy as np

from openpyxl.styles import Font

# from openpyxl import load_workbook
# from openpyxl.styles import Font, Alignment
# from openpyxl.styles.numbers import builtin_format_code

from _RF_loss_Spec import *
import _Function as func
from datetime import datetime


def Daseul_plot_figure(filename):
    font_style = Font(
        name="Calibri",
        size=10,
        bold=False,
        italic=False,
        vertAlign=None,  # 첨자
        underline="none",  # 밑줄
        strike=False,  # 취소선
        color="00000000",  # 블랙, # 00FF0000 Red, # 000000FF Blue
    )

    df_BtoB_1st = pd.DataFrame()
    df_BtoB_2nd = pd.DataFrame()
    df_RFSW1 = pd.DataFrame()

    if filename:
        for FileNumber, file in enumerate(filename):
            fname_only = os.path.basename(file).split(".")[0]
            Model = fname_only.split("_")[0]
            # Import Data
            my_cols = [str(i) for i in range(12)]  # create some col names
            df_Data = pd.read_csv(file, sep="\t|,", names=my_cols, header=None, engine="python")
            # 캘 도중 에러 발생 시 첫 열에 Nan 데이터 저장되서 count 에러 발생함 -> Drop 처리
            df_Data.drop(df_Data[df_Data["0"].isnull()].index, inplace=True)
            df_Data = df_Data.reset_index(drop=True)
            count = df_Data[df_Data["0"].str.contains("// << Equipment Loss Table - B to B >>")].shape[0]
            Re_count = df_Data[df_Data["0"].str.contains("// Re-Test")].shape[0]
            # Spec.은 for문에 넣어서 count 마다 업데이트 할 수 있지만, 최종값으로 덮어쓰기 되기 때문에 1번만 실행하는 것으로 수정함.
            Type_Read = df_Data[df_Data["0"].str.contains("RF Cable Type")].iloc[:, :2].reset_index(drop=True)

            if Type_Read.iloc[0, 1].strip() != "N/A":
                Type_Cable = int(Type_Read.iloc[0, 1].strip())
            else:
                Type_Cable = "N/A"
            Type_BtoB = int(Type_Read.iloc[1, 1].strip())
            Jig_list = df_Data[df_Data["0"].str.contains("JIG :")].iloc[:, :1]
            lineip_list = df_Data[df_Data["0"].str.contains("RDM_LOT :")].iloc[:, :1]

            if (Type_BtoB == 18) or (Type_BtoB == 19):
                BtoB_Size = 98
            elif Type_BtoB == 62:
                BtoB_Size = 129
            else:
                BtoB_Size = 58

            if Type_Cable == 7:
                RFSW_Size = 98
            elif Type_Cable == 62:
                RFSW_Size = 129
            else:
                RFSW_Size = 58

            if Type_Cable != "N/A":  # ? BtoB + RF Cable Case
                Spec_BtoB_L, Spec_BtoB_H = Type_value("BtoB", Type_BtoB)
                Spec_Cable_L, Spec_Cable_H = Type_value("RF_Cable", Type_Cable)

                BtoB1 = df_Data.index[(df_Data["0"] == "// << Equipment Loss Table - B to B >>")].to_list()
                BtoB2 = df_Data.index[(df_Data["0"] == "// << Equipment Loss Table - B to B 2 >>")].to_list()
                RFSW = df_Data.index[(df_Data["0"] == "// << Equipment Loss Table >>")].to_list()
                End_of_log = df_Data.index[(df_Data["0"].str.contains("//Total :"))].to_list()

                for Number in range(count - Re_count):
                    if Number == count - 1:
                        df_Check = df_Data.iloc[BtoB1[Number] + 3 :, :2]
                    else:
                        df_Check = df_Data.iloc[BtoB1[Number] + 3 : End_of_log[Number], :2]

                    Re_test = any(df_Check["0"].str.contains("// Re-Test"))

                    if Re_test:
                        # ! Re-test 라면 BtoB1을 다음 인덱스 값으로 넘긴다.
                        del BtoB1[Number]

                    Jig = Jig_list.iloc[Number].to_list()[0].strip()
                    lineip = lineip_list.iloc[Number].to_list()[0].split(":")[1]
                    lineip = lineip.split("_")[0].strip()

                    BtoB1_Start = BtoB1[Number] + 3
                    BtoB1_Stop = BtoB1_Start + BtoB_Size
                    df_BtoB1 = df_Data.iloc[BtoB1_Start:BtoB1_Stop, :2]

                    BtoB1_Value = df_BtoB1.iloc[:, 1:].reset_index(drop=True)
                    BtoB1_Value = BtoB1_Value.astype(float)
                    BtoB1_Value.columns = [f"{Model}_IP_{lineip}_{Jig}"]
                    BtoB1_Item = df_BtoB1["0"].str.split(" ", expand=True)
                    BtoB1_Item = BtoB1_Item.iloc[:, 3:4].reset_index(drop=True)
                    BtoB1_Item.columns = ["Frequency"]
                    df_BtoB_1st = pd.concat([df_BtoB_1st, BtoB1_Value], axis=1)

                    if BtoB2:
                        BtoB2_Start = BtoB2[Number] + 3
                        BtoB2_Stop = BtoB2_Start + BtoB_Size
                        df_BtoB2 = df_Data.iloc[BtoB2_Start:BtoB2_Stop, :2]
                        BtoB2_Value = df_BtoB2.iloc[:, 1:].reset_index(drop=True)
                        BtoB2_Value = BtoB2_Value.astype(float)
                        BtoB2_Value.columns = [f"{Model}_IP_{lineip}_{Jig}"]
                        BtoB2_Item = df_BtoB2["0"].str.split(" ", expand=True)
                        BtoB2_Item = BtoB2_Item.iloc[:, 3:4].reset_index(drop=True)
                        BtoB2_Item.columns = ["Frequency"]
                        df_BtoB_2nd = pd.concat([df_BtoB_2nd, BtoB2_Value], axis=1)
                        Check_BtoB2 = True
                    else:
                        BtoB2_Item = BtoB1_Item
                        Check_BtoB2 = False

                    RFSW_Start = RFSW[Number] + 3
                    RFSW_Stop = RFSW_Start + RFSW_Size
                    df_RFSW = df_Data.iloc[RFSW_Start:RFSW_Stop, :2]
                    RFSW_Value = df_RFSW.iloc[:, 1:].reset_index(drop=True)
                    RFSW_Value = RFSW_Value.astype(float)
                    RFSW_Value.columns = [f"{Model}_IP_{lineip}_{Jig}"]
                    RFSW_Item = df_RFSW["0"].str.split(" ", expand=True)
                    RFSW_Item = RFSW_Item.iloc[:, 2:3].reset_index(drop=True)
                    RFSW_Item.columns = ["Frequency"]
                    df_RFSW1 = pd.concat([df_RFSW1, RFSW_Value], axis=1)

                Check_RFSW1 = True
            else:  # ? BtoB + BtoB Case
                Spec_BtoB_L, Spec_BtoB_H = Type_value("BtoB", Type_BtoB)

                BtoB1 = df_Data.index[(df_Data["0"] == "// << Equipment Loss Table - B to B >>")].to_list()
                BtoB2 = df_Data.index[(df_Data["0"] == "// << Equipment Loss Table - B to B 2 >>")].to_list()
                End_of_log = df_Data.index[(df_Data["0"].str.contains("//Total :"))].to_list()

                for Number in range(count - Re_count):
                    if Number == count - 1:
                        df_Check = df_Data.iloc[BtoB1[Number] + 3 :, :2]
                    else:
                        df_Check = df_Data.iloc[BtoB1[Number] + 3 : End_of_log[Number], :2]

                    Re_test = any(df_Check["0"].str.contains("// Re-Test"))

                    if Re_test:
                        # ! Re-test 라면 BtoB1을 다음 인덱스 값으로 넘긴다.
                        del BtoB1[Number]

                    Jig = Jig_list.iloc[Number].to_list()[0].strip()
                    lineip = lineip_list.iloc[Number].to_list()[0].split(":")[1]
                    lineip = lineip.split("_")[0].strip()

                    BtoB1_Start = BtoB1[Number] + 3
                    BtoB1_Stop = BtoB1_Start + BtoB_Size
                    df_BtoB1 = df_Data.iloc[BtoB1_Start:BtoB1_Stop, :2]

                    BtoB1_Value = df_BtoB1.iloc[:, 1:].reset_index(drop=True)
                    BtoB1_Value = BtoB1_Value.astype(float)
                    BtoB1_Value.columns = [f"{Model}_IP_{lineip}_{Jig}"]
                    BtoB1_Item = df_BtoB1["0"].str.split(" ", expand=True)
                    BtoB1_Item = BtoB1_Item.iloc[:, 3:4].reset_index(drop=True)
                    BtoB1_Item.columns = ["Frequency"]
                    df_BtoB_1st = pd.concat([df_BtoB_1st, BtoB1_Value], axis=1)

                    if BtoB2:  # ! 리스트 BtoB2가 비어있지 않으면
                        BtoB2_Start = BtoB2[Number] + 3
                        BtoB2_Stop = BtoB2_Start + BtoB_Size
                        df_BtoB2 = df_Data.iloc[BtoB2_Start:BtoB2_Stop, :2]
                        BtoB2_Value = df_BtoB2.iloc[:, 1:].reset_index(drop=True)
                        BtoB2_Value = BtoB2_Value.astype(float)
                        BtoB2_Value.columns = [f"{Model}_IP_{lineip}_{Jig}"]
                        BtoB2_Item = df_BtoB2["0"].str.split(" ", expand=True)
                        BtoB2_Item = BtoB2_Item.iloc[:, 3:4].reset_index(drop=True)
                        BtoB2_Item.columns = ["Frequency"]
                        df_BtoB_2nd = pd.concat([df_BtoB_2nd, BtoB2_Value], axis=1)
                        Check_BtoB2 = True
                    else:
                        BtoB2_Item = BtoB1_Item
                        Check_BtoB2 = False

                Check_RFSW1 = False
        # plot 의 옵션들은 for문 완료 후에 1번만 수행하기 위해 따로 조건문으로 실행
        if Type_Cable == "N/A":  # ? BtoB Only
            # RF Cable Type이 N/A 인 경우 Plot창 1개
            df_BtoB_1st = df_BtoB_1st.loc[:, ~df_BtoB_1st.T.duplicated()]
            df_BtoB_2nd = df_BtoB_2nd.loc[:, ~df_BtoB_2nd.T.duplicated()]

            df_BtoB_1st = pd.merge(BtoB1_Item, df_BtoB_1st, left_index=True, right_index=True).reset_index(drop=True)
            df_BtoB_2nd = pd.merge(BtoB2_Item, df_BtoB_2nd, left_index=True, right_index=True).reset_index(drop=True)
            # X_index 를 주파수로 설정할때 사용
            BtoB1_Freq = df_BtoB_1st["Frequency"].str.split(".00MHz", expand=True).iloc[:, :1].astype(int).to_numpy()[:, 0]
            BtoB2_Freq = df_BtoB_2nd["Frequency"].str.split(".00MHz", expand=True).iloc[:, :1].astype(int).to_numpy()[:, 0]
            # 중복열 삭제 후 카운트 리셋을 위해 0 으로 세팅, for으로 +1씩 증가
            fig = go.Figure(layout=go.Layout(title=go.layout.Title(text=f"BtoB Type{Type_BtoB} Measured loss")))
            Plot_count = 0
            for i in range(1, df_BtoB_1st.shape[1], 1):
                # fill_between 사용할 수 있도록 np로 변경
                np_BtoB1 = df_BtoB_1st.iloc[:, [i]].to_numpy(dtype="float")[:, 0]
                BtoB1_index = np.arange(0, len(np_BtoB1), 1)
                np_BtoB2 = df_BtoB_2nd.iloc[:, [i]].to_numpy(dtype="float")[:, 0]
                BtoB2_index = np.arange(0, len(np_BtoB2), 1)
                fig.add_trace(
                    go.Scatter(
                        x=BtoB1_index,
                        y=np_BtoB1,
                        mode="lines+markers",
                        name=f"{df_BtoB_1st.columns[i]}",
                        showlegend=False,
                        legendgroup="BtoB",
                    )
                )

                if all(np_BtoB1 != np_BtoB2):
                    fig.add_trace(
                        go.Scatter(
                            x=BtoB2_index,
                            y=np_BtoB2,
                            mode="lines+markers",
                            name=f"{df_BtoB_2nd.columns[i]}",
                            showlegend=False,
                            legendgroup="BtoB",
                        )
                    )
                if i == 1:
                    BtoB1_y1 = min(np_BtoB1)
                    BtoB1_y2 = max(np_BtoB1)
                else:
                    BtoB1_y1 = min(BtoB1_y1, min(np_BtoB1))
                    BtoB1_y2 = max(BtoB1_y2, max(np_BtoB1))
                Plot_count += 1

            if int(Type_BtoB) == 62:
                loss_offset = np.round(Type_offset("BtoB", Type_BtoB), 2)
                Spec_BtoB_L = np.round([a + b for a, b in zip(np.round(Spec_BtoB_L, 2), np.round(loss_offset, 2))], 2)
                Spec_BtoB_H = np.round([a + b for a, b in zip(np.round(Spec_BtoB_H, 2), np.round(loss_offset, 2))], 2)
                Uder4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [98])[0]
                Over4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [97])[1]
                Over4p2G_BtoB_L = np.split(Spec_BtoB_L, [97])[1]
                Over4p2G_BtoB_H = np.split(Spec_BtoB_H, [97])[1]
            else:
                Uder4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [67])[0]
                Over4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [66])[1]
                Over4p2G_BtoB_L = np.split(Spec_BtoB_L, [66])[1]
                Over4p2G_BtoB_H = np.split(Spec_BtoB_H, [66])[1]

            fig.add_trace(
                go.Scatter(
                    x=Uder4p2G_Xindex_BtoB1,
                    y=Spec_BtoB_L,
                    mode="lines",
                    name=f"Spec_BtoB_L",
                    fill="none",  # fill area between trace0 and trace1
                    fillcolor="rgba(209, 224, 249, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=Uder4p2G_Xindex_BtoB1,
                    y=Spec_BtoB_H,
                    mode="lines",
                    name=f"Spec_BtoB_H",
                    fill="tonexty",  # fill area between trace0 and trace1
                    fillcolor="rgba(209, 224, 249, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=Over4p2G_Xindex_BtoB1,
                    y=Over4p2G_BtoB_L,
                    mode="lines",
                    name=f"Spec_BtoB_L",
                    fill="none",  # fill area between trace0 and trace1
                    fillcolor="rgba(247, 232, 236, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                )
            )
            fig.add_trace(
                go.Scatter(
                    x=Over4p2G_Xindex_BtoB1,
                    y=Over4p2G_BtoB_H,
                    mode="lines",
                    name=f"Spec_BtoB_H",
                    fill="tonexty",  # fill area between trace0 and trace1
                    fillcolor="rgba(247, 232, 236, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                )
            )

            fig.update_xaxes(
                mirror=True,
                ticks="outside",
                showline=True,
                linecolor="black",
                gridcolor="lightgrey",
                showgrid=False,
                zeroline=False,
            )
            fig.update_yaxes(
                mirror=True,
                ticks="outside",
                showline=True,
                linecolor="black",
                gridcolor="lightgrey",
                showgrid=False,
                zeroline=False,
            )

            # Axis limits
            BtoB1_x1 = min(BtoB1_index)
            BtoB1_x2 = max(BtoB1_index)
            BtoB1_ymin = floor(min(BtoB1_y1, min(Spec_BtoB_L)))
            BtoB1_ymax = ceil(max(BtoB1_y2, max(Spec_BtoB_H)))

            # Draw Horizontal Tick lines
            for k in range(int(BtoB1_ymin) + 1, int(BtoB1_ymax), 1):
                fig.add_hline(y=int(k), opacity=0.5, line_width=1, line_dash="dot", line_color="black")

            for l in range(int(BtoB1_x1), int(BtoB1_x2), 6):
                fig.add_vline(x=BtoB1_index[l], opacity=0.5, line_width=1, line_dash="dot", line_color="black")

            fig.update_layout(
                xaxis=dict(tickmode="array", ticktext=BtoB1_Freq, tickvals=BtoB1_index),
                hovermode="x unified",
                legend_traceorder="normal",
                hoverlabel=dict(namelength=-1),
            )
            fig.update_layout(
                autosize=False, width=1600, height=900, template="plotly_white", margin=dict(l=30, r=40, t=50, b=20)
            )

        else:  # ? BtoB + RF Cable
            # RF Cable Type이 N/A가 아닌 경우는 Plot창 2개
            df_BtoB_1st = df_BtoB_1st.loc[:, ~df_BtoB_1st.T.duplicated()]
            df_BtoB_2nd = df_BtoB_2nd.loc[:, ~df_BtoB_2nd.T.duplicated()]
            df_RFSW1 = df_RFSW1.loc[:, ~df_RFSW1.T.duplicated()]

            df_BtoB_1st = pd.merge(BtoB1_Item, df_BtoB_1st, left_index=True, right_index=True).reset_index(drop=True)
            df_BtoB_2nd = pd.merge(BtoB2_Item, df_BtoB_2nd, left_index=True, right_index=True).reset_index(drop=True)
            df_RFSW1 = pd.merge(RFSW_Item, df_RFSW1, left_index=True, right_index=True).reset_index(drop=True)
            # X_index 를 주파수로 설정할때 사용
            RFSW1_Freq = df_RFSW1["Frequency"].str.split(".00MHz", expand=True).iloc[:, :1].astype(int).to_numpy()[:, 0]
            BtoB1_Freq = df_BtoB_1st["Frequency"].str.split(".00MHz", expand=True).iloc[:, :1].astype(int).to_numpy()[:, 0]
            BtoB2_Freq = df_BtoB_2nd["Frequency"].str.split(".00MHz", expand=True).iloc[:, :1].astype(int).to_numpy()[:, 0]

            fig = make_subplots(
                rows=1,
                cols=2,
                horizontal_spacing=0.02,
                # specs=[[{}, {}], [{"colspan": 2}, None]], # 2 x 2
                subplot_titles=(f"BtoB Type{Type_BtoB} Measured loss", f"RFSW Type {Type_Cable} Measured loss"),
            )
            # 중복열 삭제 후 카운트 리셋을 위해 0 으로 세팅, for으로 +1씩 증가
            Plot_count = 0

            for i in range(1, df_BtoB_1st.shape[1], 1):
                # fill_between 사용할 수 있도록 np로 변경
                np_BtoB1 = df_BtoB_1st.iloc[:, [i]].to_numpy(dtype="float")[:, 0].astype(float)
                BtoB1_index = np.arange(0, len(np_BtoB1), 1)
                np_RFSW1 = df_RFSW1.iloc[:, [i]].to_numpy(dtype="float")[:, 0].astype(float)
                RFSW1_index = np.arange(0, len(np_RFSW1), 1)

                fig.add_trace(
                    go.Scatter(
                        x=BtoB1_index,
                        y=np_BtoB1,
                        customdata=BtoB1_Freq,
                        mode="lines+markers",
                        name=f"{df_BtoB_1st.columns[i]}",
                        showlegend=False,
                        legendgroup="BtoB",
                    ),
                    row=1,
                    col=1,
                )
                fig.add_trace(
                    go.Scatter(
                        x=RFSW1_index,
                        y=np_RFSW1,
                        customdata=RFSW1_Freq,
                        mode="lines+markers",
                        name=f"{df_RFSW1.columns[i]}",
                        showlegend=False,
                        legendgroup="RFSW",
                    ),
                    row=1,
                    col=2,
                )
                if i == 1:
                    BtoB1_y1 = min(np_BtoB1)
                    BtoB1_y2 = max(np_BtoB1)
                    RFSW1_y1 = min(np_RFSW1)
                    RFSW1_y2 = max(np_RFSW1)
                else:
                    BtoB1_y1 = min(BtoB1_y1, min(np_BtoB1))
                    BtoB1_y2 = max(BtoB1_y2, max(np_BtoB1))
                    RFSW1_y1 = min(RFSW1_y1, min(np_RFSW1))
                    RFSW1_y2 = max(RFSW1_y2, max(np_RFSW1))
                Plot_count += 1

            if int(Type_Cable) == 62:
                loss_offset = np.round(Type_offset("BtoB", Type_BtoB), 2)
                Spec_BtoB_L = np.round([a + b for a, b in zip(np.round(Spec_BtoB_L, 2), np.round(loss_offset, 2))], 2)
                Spec_BtoB_H = np.round([a + b for a, b in zip(np.round(Spec_BtoB_H, 2), np.round(loss_offset, 2))], 2)
                Uder4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [98])[0]
                Over4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [97])[1]
                Over4p2G_BtoB_L = np.split(Spec_BtoB_L, [97])[1]
                Over4p2G_BtoB_H = np.split(Spec_BtoB_H, [97])[1]

                RFSW_loss_offset = np.round(Type_offset("RF_Cable", Type_Cable), 2)
                Spec_Cable_L = np.round([a + b for a, b in zip(np.round(Spec_Cable_L, 2), np.round(RFSW_loss_offset, 2))], 2)
                Spec_Cable_H = np.round([a + b for a, b in zip(np.round(Spec_Cable_H, 2), np.round(RFSW_loss_offset, 2))], 2)
                Uder4p2G_Xindex_RFSW1 = np.split(RFSW1_index, [98])[0]
                Over4p2G_Xindex_RFSW1 = np.split(RFSW1_index, [97])[1]
                Over4p2G_Cable_L = np.split(Spec_Cable_L, [97])[1]
                Over4p2G_Cable_H = np.split(Spec_Cable_H, [97])[1]
            else:
                Uder4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [67])[0]
                Over4p2G_Xindex_BtoB1 = np.split(BtoB1_index, [66])[1]
                Over4p2G_BtoB_L = np.split(Spec_BtoB_L, [66])[1]
                Over4p2G_BtoB_H = np.split(Spec_BtoB_H, [66])[1]

                Uder4p2G_Xindex_RFSW1 = np.split(RFSW1_index, [67])[0]
                Over4p2G_Xindex_RFSW1 = np.split(RFSW1_index, [66])[1]
                Over4p2G_Cable_L = np.split(Spec_Cable_L, [66])[1]
                Over4p2G_Cable_H = np.split(Spec_Cable_H, [66])[1]

            fig.add_trace(
                go.Scatter(
                    x=Uder4p2G_Xindex_BtoB1,
                    y=Spec_BtoB_L,
                    mode="lines",
                    name=f"Spec_BtoB_L",
                    fill="none",  # fill area between trace0 and trace1
                    fillcolor="rgba(209, 224, 249, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=Uder4p2G_Xindex_BtoB1,
                    y=Spec_BtoB_H,
                    mode="lines",
                    name=f"Spec_BtoB_H",
                    fill="tonexty",  # fill area between trace0 and trace1
                    fillcolor="rgba(209, 224, 249, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=Over4p2G_Xindex_BtoB1,
                    y=Over4p2G_BtoB_L,
                    mode="lines",
                    name=f"Spec_BtoB_L",
                    fill="none",  # fill area between trace0 and trace1
                    fillcolor="rgba(247, 232, 236, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=Over4p2G_Xindex_BtoB1,
                    y=Over4p2G_BtoB_H,
                    mode="lines",
                    name=f"Spec_BtoB_H",
                    fill="tonexty",  # fill area between trace0 and trace1
                    fillcolor="rgba(247, 232, 236, 0.3)",
                    showlegend=False,
                    legendgroup="BtoB",
                ),
                row=1,
                col=1,
            )
            fig.add_trace(
                go.Scatter(
                    x=Uder4p2G_Xindex_RFSW1,
                    y=Spec_Cable_L,
                    mode="lines",
                    name=f"Spec_RFSW_L",
                    fill="none",  # fill area between trace0 and trace1
                    fillcolor="rgba(209, 224, 249, 0.3)",
                    showlegend=False,
                    legendgroup="RFSW",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=Uder4p2G_Xindex_RFSW1,
                    y=Spec_Cable_H,
                    mode="lines",
                    name=f"Spec_RFSW_H",
                    fill="tonexty",  # fill area between trace0 and trace1
                    fillcolor="rgba(209, 224, 249, 0.3)",
                    showlegend=False,
                    legendgroup="RFSW",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=Over4p2G_Xindex_RFSW1,
                    y=Over4p2G_Cable_L,
                    mode="lines",
                    name=f"Spec_RFSW_L",
                    fill="none",  # fill area between trace0 and trace1
                    fillcolor="rgba(247, 232, 236, 0.3)",
                    showlegend=False,
                    legendgroup="RFSW",
                ),
                row=1,
                col=2,
            )
            fig.add_trace(
                go.Scatter(
                    x=Over4p2G_Xindex_RFSW1,
                    y=Over4p2G_Cable_H,
                    mode="lines",
                    name=f"Spec_RFSW_H",
                    fill="tonexty",  # fill area between trace0 and trace1
                    fillcolor="rgba(247, 232, 236, 0.3)",
                    showlegend=False,
                    legendgroup="RFSW",
                ),
                row=1,
                col=2,
            )
            fig.update_xaxes(
                mirror=True,
                ticks="outside",
                showline=True,
                linecolor="black",
                gridcolor="lightgrey",
                showgrid=False,
                zeroline=False,
            )
            fig.update_yaxes(
                mirror=True,
                ticks="outside",
                showline=True,
                linecolor="black",
                gridcolor="lightgrey",
                showgrid=False,
                zeroline=False,
            )

            # Axis limits
            BtoB1_x1 = min(BtoB1_index)
            BtoB1_x2 = max(BtoB1_index)
            BtoB1_ymin = floor(min(BtoB1_y1, min(Spec_BtoB_L)))
            BtoB1_ymax = ceil(max(BtoB1_y2, max(Spec_BtoB_H)))
            # RFSW1_x1 = min(RFSW1_index)
            # RFSW1_x2 = max(RFSW1_index)
            # RFSW1_ymin = floor(min(RFSW1_y1, min(Spec_BtoB_L)))
            # RFSW1_ymax = ceil(max(RFSW1_y2, max(Spec_BtoB_H)))

            # Draw Horizontal Tick lines
            for k in range(int(BtoB1_ymin) + 1, int(BtoB1_ymax), 1):
                fig.add_hline(y=int(k), opacity=0.5, line_width=1, line_dash="dot", line_color="black")

            for l in range(int(BtoB1_x1), int(BtoB1_x2), 6):
                fig.add_vline(x=BtoB1_index[l], opacity=0.5, line_width=1, line_dash="dot", line_color="black")

            fig.update_layout(
                xaxis=dict(tickmode="array", ticktext=BtoB1_Freq, tickvals=BtoB1_index),
                xaxis2=dict(tickmode="array", ticktext=RFSW1_Freq, tickvals=RFSW1_index),
                hovermode="x unified",
                legend_traceorder="normal",
                hoverlabel=dict(namelength=-1),
            )
            fig.update_layout(
                autosize=False, width=3200, height=900, template="plotly_white", margin=dict(l=30, r=40, t=50, b=20)
            )
        # fig.update_traces(hoverinfo = 'name+y')
        fig.show()

        f_name = f"{os.path.splitext(filename[0])[0]}_loss.html"  # filename을 확장자를 지운 후 pdf 확장자로 지정
        plotly.offline.plot(fig, filename=f_name, auto_open=False)
        # fig.write_image(f_name)
        dir, file = os.path.split((f_name))
        Model = file.split("_")[0]
        timecheck = datetime.now().strftime("%Y-%m%d_%H%M")

        # Save Data to Excel
        Excel_file = f"Export_{Model}_Daseul_{timecheck}.xlsx"
        with pd.ExcelWriter(Excel_file, engine="openpyxl") as writer:
            df_BtoB_1st.to_excel(writer, sheet_name="BtoB1")
            if Check_BtoB2:
                df_BtoB_2nd.to_excel(writer, sheet_name="BtoB2")
            if Check_RFSW1:
                df_RFSW1.to_excel(writer, sheet_name="RFSW")
        func.WB_Format(Excel_file, 2, 2, 2)

    # func.open_file(f_name)
