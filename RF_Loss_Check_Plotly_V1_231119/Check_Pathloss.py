import os
from math import ceil, floor

import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
import numpy as np

from openpyxl.styles import Font
# from openpyxl import load_workbook
# from openpyxl.styles.numbers import builtin_format_code

import tkinter.messagebox as msgbox

from _RF_loss_Spec import *
import _Function as func
from datetime import datetime


def Pathloss_Plot_figure(filename, Result_var):
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

    df_BtoB1 = pd.DataFrame()

    if filename:
        for FileNumber, file in enumerate(filename):
            fname_only = os.path.basename(file).split(".")[0]
            # Import Data
            my_cols = [str(i) for i in range(10)]  # create some col names
            df_Data = pd.read_csv(file, sep="\t|,", names=my_cols, header=None, engine="python")
            Current_Type = df_Data[df_Data["0"].str.contains("Current Cable Type", na=False)]
            Current_Type = Current_Type["0"].str.split(":", expand=True).iloc[0, 1].strip()
            df_Test = df_Data.index[(df_Data["0"] == "#TEST")].to_list()

            if df_Data["0"].str.contains("SVC", na=False).any():
                df_Cabletype = df_Data[df_Data["0"].str.contains("RF Cable Type BtoB : ", na=False)].iloc[:, :1]
                Type_SVC = True
            elif Current_Type == "BtoB":
                df_Cabletype = df_Data[df_Data["0"].str.contains("RF Cable Type BtoB : ", na=False)].iloc[:, :1]
                Type_SVC = False
            else:
                df_Cabletype = df_Data[df_Data["0"].str.contains("RF Cable Type : ", na=False)].iloc[:, :1]
                Type_SVC = False

            Jig_list = df_Data[df_Data["0"].str.contains("JIG :", na=False)].iloc[:, :1]
            Result = df_Data[df_Data["0"].str.contains("RESULT :", na=False)].iloc[:, :1]
            lineip_list = df_Data[df_Data["0"].str.contains("RDM_LOT :", na=False)].iloc[:, :1]

            for Count, index in enumerate(df_Test):
                # for index in BtoB1:
                LossCal_Result = Result.iloc[Count].to_list()[0].split(":")[1]
                lineip = lineip_list.iloc[Count].to_list()[0].split(":")[1]
                lineip = lineip.split("_")[0].strip()

                if Result_var.get():
                    if Type_SVC:
                        BtoB_Type = "SVC"
                    else:
                        BtoB_Type = "BtoB"

                    Type = int(df_Cabletype.iloc[Count].to_list()[0].split(":")[1].strip())
                    Jig = Jig_list.iloc[Count].to_list()[0].strip()

                    if (Type == 18) or (Type == 19):
                        Size = 98
                    elif Type == 7:
                        Size = 98
                    elif Type == 62:
                        Size = 129
                    else:
                        Size = 58

                    Loss_Start = index + 3
                    Loss_Stop = Loss_Start + Size
                    df_BtoB_1st = df_Data.iloc[Loss_Start:Loss_Stop, :4]
                    BtoB1st_Value = df_BtoB_1st.iloc[:, 1:2].reset_index(drop=True).astype(float)
                    # BtoB1st_Value = BtoB1st_Value.astype(float)
                    BtoB1st_Value.columns = [f"{fname_only}_IP_{lineip}_{Jig}"]
                    # Variance 측정을 위한 Dataframe
                    Var_Table = BtoB1st_Value[f"{fname_only}_IP_{lineip}_{Jig}"][0:18]
                    Variance = np.var(Var_Table)
                    BtoB1st_Item = df_BtoB_1st["0"].str.split(" ", expand=True).reset_index(drop=True)
                    BtoB1st_Item[4] = BtoB1st_Item[4].str.replace(pat=r"[^\w]|Loss", repl=r"", regex=True)

                    if BtoB1st_Item[0].str.contains("SVC", na=False).any():
                        BtoB1st_Item.columns = ["SVC", "Meas", "BtoB_No", "Path", "Frequency"]
                    elif Current_Type == "BtoB":
                        BtoB1st_Item.columns = ["Meas", "BtoB_No", "Path", "Frequency"]
                    else:
                        BtoB1st_Item.columns = ["Meas", "Path", "Frequency"]

                    BtoB1st_Item = BtoB1st_Item[["Frequency"]]
                    # BtoB1st_Item.drop(columns=["Meas", "Path"], inplace=True)
                    df_BtoB1 = pd.concat([df_BtoB1, BtoB1st_Value], axis=1)
                    # fill_between 사용할 수 있도록 np로 변경

                else:
                    if LossCal_Result == "FAIL":
                        msgbox.showwarning("Warning", f"Losscal Result : Fail\nOr\nCheck 'Include Failed log' Button")
                        # plt.close()
                        return
                    else:
                        if Type_SVC:
                            BtoB_Type = "SVC"
                        else:
                            BtoB_Type = "BtoB"

                        Type = int(df_Cabletype.iloc[Count].to_list()[0].split(":")[1].strip())
                        Jig = Jig_list.iloc[Count].to_list()[0].strip()

                        if (Type == 18) or (Type == 19):
                            Size = 98
                        elif Type == 7:
                            Size = 98
                        elif Type == 62:
                            Size = 129
                        else:
                            Size = 58

                        Loss_Start = index + 3
                        Loss_Stop = Loss_Start + Size
                        df_BtoB_1st = df_Data.iloc[Loss_Start:Loss_Stop, :4]
                        BtoB1st_Value = df_BtoB_1st.iloc[:, 1:2].reset_index(drop=True)
                        BtoB1st_Value = BtoB1st_Value.astype(float)
                        BtoB1st_Value.columns = [f"{fname_only}_IP_{lineip}_{Jig}"]
                        # Variance 측정을 위한 Dataframe
                        Var_Table = BtoB1st_Value[f"{fname_only}_IP_{lineip}_{Jig}"][0:18]
                        Variance = np.var(Var_Table)
                        BtoB1st_Item = df_BtoB_1st["0"].str.split(" ", expand=True).reset_index(drop=True)

                        if BtoB1st_Item[0].str.contains("SVC", na=False).any():
                            BtoB1st_Item.columns = ["SVC", "Meas", "BtoB_No", "Path", "Frequency"]
                        elif Current_Type == "BtoB":
                            BtoB1st_Item.columns = ["Meas", "BtoB_No", "Path", "Frequency"]
                        else:
                            BtoB1st_Item.columns = ["Meas", "Path", "Frequency"]

                        BtoB1st_Item = BtoB1st_Item[["Frequency"]]
                        # BtoB1st_Item.drop(columns=["Meas", "Path"], inplace=True)
                        df_BtoB1 = pd.concat([df_BtoB1, BtoB1st_Value], axis=1)

        df_BtoB1 = df_BtoB1.loc[:, ~df_BtoB1.T.duplicated()]
        df_BtoB1 = pd.merge(BtoB1st_Item, df_BtoB1, left_index=True, right_index=True)
        # df_BtoB1 = df_BtoB1.style.set_properties(**{"font-size": "10pt"})
        df_BtoB1_Mean = round(df_BtoB1.groupby(["Frequency"], sort=False).mean(), 2)
        df_BtoB1_Mean["Average"] = round(df_BtoB1_Mean.mean(axis=1), 2)
        df_BtoB1_Mean["Max"] = round(df_BtoB1_Mean.max(axis=1), 2)
        df_BtoB1_Mean["Min"] = round(df_BtoB1_Mean.min(axis=1), 2)
        BtoB1_Freq = df_BtoB1["Frequency"].str.split("MHz", expand=True).iloc[:, :1].astype(int).to_numpy()[:, 0]
        loss_offset = np.round(Type_offset("SVC", Type), 2)

        fig = go.Figure(layout=go.Layout(title=go.layout.Title(text=f"{Current_Type} {BtoB_Type} {Type} PathLoss Data")))
        Count += 1
        for i in range(1, df_BtoB1.shape[1], 1):
            # fill_between 사용할 수 있도록 np로 변경
            np_BtoB1 = df_BtoB1.iloc[:, [i]].to_numpy(dtype="float")[:, 0].astype(float)
            # Daseul은 Common loss + loss offset이 적용된 값으로 Cal log에 저장되는 반면
            # Pathloss는 측정된 loss만을 cal log에 저장한다 -> loss_offset은 반영한 값으로 np_BtoB1에 재지정
            np_BtoB1 = np.round([a + b for a, b in zip(np.round(np_BtoB1, 2), np.round(loss_offset, 2))], 2)
            X_index_BtoB1 = np.arange(0, len(np_BtoB1), 1)
            fig.add_trace(
                go.Scatter(
                    x=X_index_BtoB1,
                    y=np_BtoB1,
                    mode="lines+markers",
                    name=f"{df_BtoB1.columns[i]}",
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

        Spec_L, Spec_H = Type_value(BtoB_Type, Type)

        if Type == 62:
            Spec_L = np.round([a + b for a, b in zip(np.round(Spec_L, 2), np.round(loss_offset, 2))], 2)
            Spec_H = np.round([a + b for a, b in zip(np.round(Spec_H, 2), np.round(loss_offset, 2))], 2)
            Uder4p2G_Xindex_BtoB1 = np.split(X_index_BtoB1, [98])[0]
            Over4p2G_Xindex_BtoB1 = np.split(X_index_BtoB1, [97])[1]
            Over4p2G_L = np.split(Spec_L, [97])[1]
            Over4p2G_H = np.split(Spec_H, [97])[1]
        else:
            Uder4p2G_Xindex_BtoB1 = np.split(X_index_BtoB1, [67])[0]
            Over4p2G_Xindex_BtoB1 = np.split(X_index_BtoB1, [66])[1]
            Over4p2G_L = np.split(Spec_L, [66])[1]
            Over4p2G_H = np.split(Spec_H, [66])[1]
        fig.add_trace(
            go.Scatter(
                x=Uder4p2G_Xindex_BtoB1,
                y=Spec_L,
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
                y=Spec_H,
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
                y=Over4p2G_L,
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
                y=Over4p2G_H,
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
        BtoB1_x1 = min(X_index_BtoB1)
        BtoB1_x2 = max(X_index_BtoB1)
        BtoB1_ymin = floor(min(BtoB1_y1, min(Spec_L)))
        BtoB1_ymax = ceil(max(BtoB1_y2, max(Spec_H)))

        # Draw Horizontal Tick lines
        for k in range(int(BtoB1_ymin) + 1, int(BtoB1_ymax), 1):
            fig.add_hline(y=int(k), opacity=0.5, line_width=1, line_dash="dot", line_color="black")

        for l in range(int(BtoB1_x1), int(BtoB1_x2), 6):
            fig.add_vline(x=X_index_BtoB1[l], opacity=0.5, line_width=1, line_dash="dot", line_color="black")

        fig.update_layout(
            xaxis=dict(tickmode="array", ticktext=BtoB1_Freq, tickvals=X_index_BtoB1),
            hovermode="x unified",
            legend_traceorder="normal",
            hoverlabel=dict(namelength=-1, font_family="Consolas"),
        )
        fig.update_layout(autosize=False, width=1600, height=900, template="plotly_white", margin=dict(l=30, r=40, t=50, b=20))
        fig.show()

        f_name = f"{os.path.splitext(filename[0])[0]}_loss.html"  # filename을 확장자를 지운 후 pdf 확장자로 지정
        plotly.offline.plot(fig, filename=f_name, auto_open=False)
        # fig.write_image(f_name)
        dir, file = os.path.split((f_name))
        Model = file.split("_")[0]
        timecheck = datetime.now().strftime("%Y-%m%d_%H%M")

        # Save Data to Excel
        Excel_file = f"Export_{Model}_Pathloss_{timecheck}.xlsx"
        with pd.ExcelWriter(Excel_file) as writer:
            df_BtoB1_Mean.to_excel(writer, sheet_name="BtoB1_Mean")
        func.WB_Format(Excel_file, 2, 2, 2)
    # func.open_file(f_name)
