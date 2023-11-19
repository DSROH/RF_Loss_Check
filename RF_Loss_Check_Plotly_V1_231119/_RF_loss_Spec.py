def Type_value(Type, Current_Type):
    dict_spec = {
        "SVC": {
            16: {"Spec_L": [-12.81, -13.06, -13.19, -13.22, -13.24, -13.21, -13.30, -13.33, -13.36, -13.42, -13.45, -13.48, -13.51, -13.57, -13.75, -13.73, -13.71, -13.75, -13.92, -14.64, -14.72, -14.73, -14.74, -14.80, -15.25, -15.58, -15.54, -15.99, -15.89, -15.88, -15.79, -15.66, -15.85, -15.53, -15.80, -15.88, -16.05, -15.82, -16.12, -16.69, -16.32, -16.01, -16.32, -16.14, -16.12, -16.28, -16.27, -18.28, -18.92, -17.66, -19.03, -18.23, -18.14, -18.91, -17.61, -18.93, -18.21, -19.39, -19.47, -19.16, -19.98, -19.44, -19.55, -19.60, -18.96, -19.49, -19.69, -19.74, -20.55, -19.35, -19.61, -19.53, -18.98, -19.91, -19.47, -19.93, -20.21, -20.31, -20.44, -21.37, -20.63, -21.09, -21.51, -21.08, -21.92, -20.10, -21.44, -20.86, -20.73, -21.91, -20.64, -21.44, -21.80, -22.08, -21.64, -22.29, -22.85, -23.98], "Spec_H": [-9.81, -10.06, -10.19, -10.22, -10.24, -10.21, -10.30, -10.33, -10.36, -10.42, -10.45, -10.48, -10.51, -10.57, -10.75, -10.73, -10.71, -10.75, -10.92, -11.64, -11.72, -11.73, -11.74, -11.80, -12.25, -12.58, -12.54, -12.99, -12.89, -12.88, -12.79, -12.66, -12.85, -12.53, -12.80, -12.88, -13.05, -12.82, -13.12, -13.69, -13.32, -13.01, -13.32, -13.14, -13.12, -13.28, -13.27, -12.28, -12.92, -11.66, -13.03, -12.23, -12.14, -12.91, -11.61, -12.93, -12.21, -13.39, -13.47, -13.16, -13.98, -13.44, -13.55, -13.60, -12.96, -13.49, -13.69, -13.74, -14.55, -13.35, -13.61, -13.53, -12.98, -13.91, -13.47, -13.93, -14.21, -14.31, -14.44, -15.37, -14.63, -15.09, -15.51, -15.08, -15.92, -14.10, -15.44, -14.86, -14.73, -15.91, -14.64, -15.44, -15.80, -16.08, -15.64, -16.29, -16.85, -17.98]},
            17: {"Spec_L": [-12.81, -13.06, -13.19, -13.22, -13.24, -13.21, -13.30, -13.33, -13.36, -13.42, -13.45, -13.48, -13.51, -13.57, -13.75, -13.73, -13.71, -13.75, -13.92, -14.64, -14.72, -14.73, -14.74, -14.80, -15.25, -15.58, -15.54, -15.99, -15.89, -15.88, -15.79, -15.66, -15.85, -15.53, -15.80, -15.88, -16.05, -15.82, -16.12, -16.69, -16.32, -16.01, -16.32, -16.14, -16.12, -16.28, -16.27, -18.28, -18.92, -17.66, -19.03, -18.23, -18.14, -18.91, -17.61, -18.93, -18.21, -19.39, -19.47, -19.16, -19.98, -19.44, -19.55, -19.60, -18.96, -19.49, -19.69, -19.74, -20.55, -19.35, -19.61, -19.53, -18.98, -19.91, -19.47, -19.93, -20.21, -20.31, -20.44, -21.37, -20.63, -21.09, -21.51, -21.08, -21.92, -20.10, -21.44, -20.86, -20.73, -21.91, -20.64, -21.44, -21.80, -22.08, -21.64, -22.29, -22.85, -23.98], "Spec_H": [-9.81, -10.06, -10.19, -10.22, -10.24, -10.21, -10.30, -10.33, -10.36, -10.42, -10.45, -10.48, -10.51, -10.57, -10.75, -10.73, -10.71, -10.75, -10.92, -11.64, -11.72, -11.73, -11.74, -11.80, -12.25, -12.58, -12.54, -12.99, -12.89, -12.88, -12.79, -12.66, -12.85, -12.53, -12.80, -12.88, -13.05, -12.82, -13.12, -13.69, -13.32, -13.01, -13.32, -13.14, -13.12, -13.28, -13.27, -12.28, -12.92, -11.66, -13.03, -12.23, -12.14, -12.91, -11.61, -12.93, -12.21, -13.39, -13.47, -13.16, -13.98, -13.44, -13.55, -13.60, -12.96, -13.49, -13.69, -13.74, -14.55, -13.35, -13.61, -13.53, -12.98, -13.91, -13.47, -13.93, -14.21, -14.31, -14.44, -15.37, -14.63, -15.09, -15.51, -15.08, -15.92, -14.10, -15.44, -14.86, -14.73, -15.91, -14.64, -15.44, -15.80, -16.08, -15.64, -16.29, -16.85, -17.98]},
            18: {"Spec_L": [-12.81, -13.06, -13.19, -13.22, -13.24, -13.21, -13.30, -13.33, -13.36, -13.42, -13.45, -13.48, -13.51, -13.57, -13.75, -13.73, -13.71, -13.75, -13.92, -14.64, -14.72, -14.73, -14.74, -14.80, -15.25, -15.58, -15.54, -15.99, -15.89, -15.88, -15.79, -15.66, -15.85, -15.53, -15.80, -15.88, -16.05, -15.82, -16.12, -16.69, -16.32, -16.01, -16.32, -16.14, -16.12, -16.28, -16.27, -18.28, -18.92, -17.66, -19.03, -18.23, -18.14, -18.91, -17.61, -18.93, -18.21, -19.39, -19.47, -19.16, -19.98, -19.44, -19.55, -19.60, -18.96, -19.49, -19.69, -19.74, -20.55, -19.35, -19.61, -19.53, -18.98, -19.91, -19.47, -19.93, -20.21, -20.31, -20.44, -21.37, -20.63, -21.09, -21.51, -21.08, -21.92, -20.10, -21.44, -20.86, -20.73, -21.91, -20.64, -21.44, -21.80, -22.08, -21.64, -22.29, -22.85, -23.98], "Spec_H": [-9.81, -10.06, -10.19, -10.22, -10.24, -10.21, -10.30, -10.33, -10.36, -10.42, -10.45, -10.48, -10.51, -10.57, -10.75, -10.73, -10.71, -10.75, -10.92, -11.64, -11.72, -11.73, -11.74, -11.80, -12.25, -12.58, -12.54, -12.99, -12.89, -12.88, -12.79, -12.66, -12.85, -12.53, -12.80, -12.88, -13.05, -12.82, -13.12, -13.69, -13.32, -13.01, -13.32, -13.14, -13.12, -13.28, -13.27, -12.28, -12.92, -11.66, -13.03, -12.23, -12.14, -12.91, -11.61, -12.93, -12.21, -13.39, -13.47, -13.16, -13.98, -13.44, -13.55, -13.60, -12.96, -13.49, -13.69, -13.74, -14.55, -13.35, -13.61, -13.53, -12.98, -13.91, -13.47, -13.93, -14.21, -14.31, -14.44, -15.37, -14.63, -15.09, -15.51, -15.08, -15.92, -14.10, -15.44, -14.86, -14.73, -15.91, -14.64, -15.44, -15.80, -16.08, -15.64, -16.29, -16.85, -17.98]},
            19: {"Spec_L": [-12.81, -13.06, -13.19, -13.22, -13.24, -13.21, -13.30, -13.33, -13.36, -13.42, -13.45, -13.48, -13.51, -13.57, -13.75, -13.73, -13.71, -13.75, -13.92, -14.64, -14.72, -14.73, -14.74, -14.80, -15.25, -15.58, -15.54, -15.99, -15.89, -15.88, -15.79, -15.66, -15.85, -15.53, -15.80, -15.88, -16.05, -15.82, -16.12, -16.69, -16.32, -16.01, -16.32, -16.14, -16.12, -16.28, -16.27, -18.28, -18.92, -17.66, -19.03, -18.23, -18.14, -18.91, -17.61, -18.93, -18.21, -19.39, -19.47, -19.16, -19.98, -19.44, -19.55, -19.60, -18.96, -19.49, -19.69, -19.74, -20.55, -19.35, -19.61, -19.53, -18.98, -19.91, -19.47, -19.93, -20.21, -20.31, -20.44, -21.37, -20.63, -21.09, -21.51, -21.08, -21.92, -20.10, -21.44, -20.86, -20.73, -21.91, -20.64, -21.44, -21.80, -22.08, -21.64, -22.29, -22.85, -23.98], "Spec_H": [-9.81, -10.06, -10.19, -10.22, -10.24, -10.21, -10.30, -10.33, -10.36, -10.42, -10.45, -10.48, -10.51, -10.57, -10.75, -10.73, -10.71, -10.75, -10.92, -11.64, -11.72, -11.73, -11.74, -11.80, -12.25, -12.58, -12.54, -12.99, -12.89, -12.88, -12.79, -12.66, -12.85, -12.53, -12.80, -12.88, -13.05, -12.82, -13.12, -13.69, -13.32, -13.01, -13.32, -13.14, -13.12, -13.28, -13.27, -12.28, -12.92, -11.66, -13.03, -12.23, -12.14, -12.91, -11.61, -12.93, -12.21, -13.39, -13.47, -13.16, -13.98, -13.44, -13.55, -13.60, -12.96, -13.49, -13.69, -13.74, -14.55, -13.35, -13.61, -13.53, -12.98, -13.91, -13.47, -13.93, -14.21, -14.31, -14.44, -15.37, -14.63, -15.09, -15.51, -15.08, -15.92, -14.10, -15.44, -14.86, -14.73, -15.91, -14.64, -15.44, -15.80, -16.08, -15.64, -16.29, -16.85, -17.98]},
            62: {"Spec_L": [-7.52,-7.49,-7.56,-7.61,-7.62,-7.58,-7.53,-7.64,-7.65,-7.63,-7.61,-7.65,-7.65,-7.62,-7.59,-7.65,-7.75,-7.71,-7.71,-7.74,-7.74,-8.08,-8.08,-8,-7.97,-8.05,-8,-8,-8,-8,-8,-8,-8,-8,-8.09,-8.11,-8.13,-8.13,-8.19,-8.19,-8.32,-8.28,-8.32,-8.38,-8.37,-8.4,-8.9,-8.9,-8.9,-8.78,-8.9,-8.9,-8.9,-8.91,-9.07,-9,-9.17,-9.19,-9.16,-9.27,-9.3,-9.21,-9.28,-9.65,-9.65,-9.65,-9.84,-9.57,-9.65,-9.99,-9.94,-9.71,-9.65,-9.94,-9.65,-9.87,-9.88,-10.15,-10.15,-10.15,-10.2,-10.15,-9.87,-10.15,-10.15,-10.15,-10.15,-10.15,-10.15,-10.69,-10.86,-10.99,-10.99,-10.75,-10.85,-11.01,-10.89,-11.27,-11.18,-11.34,-10.86,-11.04,-11.23,-11.22,-11.37,-11.36,-11.52,-11.46,-11.07,-11.36,-11.31,-11.02,-11.19,-11.12,-11.07,-11.31,-11.23,-11.2,-11.17,-11.35,-11.36,-11.28,-11.54,-11.96,-12.07,-12.06,-12.03,-11.96,-12.07], "Spec_H": [-5.52,-5.49,-5.56,-5.61,-5.62,-5.58,-5.53,-5.64,-5.65,-5.63,-5.61,-5.65,-5.65,-5.62,-5.59,-5.65,-5.75,-5.71,-5.71,-5.74,-5.74,-6.08,-6.08,-6,-5.97,-6.05,-6,-6,-6,-6,-6,-6,-6,-6,-6.09,-6.11,-6.13,-6.13,-6.19,-6.19,-6.32,-6.28,-6.32,-6.38,-6.37,-6.4,-5.9,-5.9,-5.9,-5.78,-5.9,-5.9,-5.9,-5.91,-6.07,-6,-6.17,-6.19,-6.16,-6.27,-6.3,-6.21,-6.28,-6.35,-6.35,-6.35,-6.54,-6.27,-6.35,-6.69,-6.64,-6.41,-6.35,-6.64,-6.35,-6.57,-6.58,-6.85,-6.85,-6.85,-6.9,-6.85,-6.57,-6.85,-6.85,-6.85,-6.85,-6.85,-6.85,-5.69,-5.86,-5.99,-5.99,-5.75,-5.85,-6.01,-5.89,-6.27,-6.18,-6.34,-5.86,-6.04,-6.23,-6.22,-6.37,-6.36,-6.52,-6.46,-6.07,-6.36,-6.31,-6.02,-6.19,-6.12,-6.07,-6.31,-6.23,-6.2,-6.17,-6.35,-6.36,-6.28,-6.54,-6.96,-7.07,-7.06,-7.03,-6.96,-7.07]},
            64: {"Spec_L": [-11.92,-11.88,-11.93,-11.98,-12.01,-12.02,-11.97,-12.12,-12.22,-12.22,-12.21,-12.01,-12.23,-12.23,-12.14,-12.15,-12.23,-12.16,-12.24,-12.26,-12.25,-12.74,-12.78,-12.69,-12.74,-12.82,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.79,-12.85,-12.84,-12.82,-12.86,-12.93,-13.08,-13.03,-13.01,-13.07,-13.09,-13.1,-13.6,-13.6,-13.6,-13.62,-13.65,-13.6,-13.6,-13.68,-13.9,-13.85,-14.01,-14.03,-13.99,-14.13,-14.15,-14.12,-14.18,-14.5,-14.5,-14.48,-14.59,-14.43,-14.5,-14.89,-14.85,-14.63,-14.5,-14.9,-14.5,-14.79,-14.79,-15,-15,-15,-15.34,-15,-14.92,-15,-15,-15,-15,-15,-15,-16.37,-16.41,-16.53,-16.56,-16.4,-16.54,-16.63,-16.53,-17.03,-16.87,-17.02,-16.6,-16.81,-16.98,-17,-17.17,-17.09,-17.17,-17.14,-16.81,-17.11,-17.04,-16.77,-16.94,-16.87,-16.81,-17.04,-16.97,-17.05,-17.06,-17.16,-17.16,-17.13,-17.34,-17.8,-18,-17.98,-17.94,-17.95,-18.08], "Spec_H": [-7.92,-7.88,-7.93,-7.98,-8.01,-8.02,-7.96,-8.12,-8.22,-8.22,-8.21,-8.01,-8.23,-8.22,-8.14,-8.15,-8.23,-8.16,-8.24,-8.26,-8.25,-8.74,-8.78,-8.69,-8.74,-8.82,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.79,-8.85,-8.84,-8.82,-8.86,-8.93,-9.08,-9.03,-9.01,-9.07,-9.09,-9.1,-8.6,-8.6,-8.6,-8.62,-8.65,-8.6,-8.6,-8.68,-8.89,-8.85,-9.01,-9.03,-8.99,-9.13,-9.15,-9.12,-9.18,-9.5,-9.5,-9.47,-9.59,-9.43,-9.5,-9.89,-9.85,-9.63,-9.5,-9.9,-9.5,-9.79,-9.79,-10,-10,-10,-10.34,-10,-9.92,-10,-10,-10,-10,-10,-10,-8.37,-8.41,-8.53,-8.55,-8.39,-8.54,-8.63,-8.53,-9.03,-8.87,-9.02,-8.6,-8.81,-8.98,-9,-9.17,-9.1,-9.17,-9.14,-8.81,-9.11,-9.04,-8.78,-8.94,-8.87,-8.81,-9.04,-8.97,-9.05,-9.06,-9.15,-9.16,-9.13,-9.34,-9.8,-10,-9.98,-9.94,-9.96,-10.08]},
        },
        "BtoB": {
            16: {"Spec_L": [-9.77, -9.84, -9.95, -10.03, -10.08, -10.12, -10.07, -10.13, -10.22, -10.2, -10.17, -10.29, -10.37, -10.38, -10.39, -10.51, -10.59, -10.46, -10.62, -11.65, -11.65, -11.64, -11.73, -11.82, -12.21, -12.43, -12.45, -12.49, -12.74, -12.7, -12.77, -12.6, -12.82, -12.66, -12.66, -13.36, -13.44, -13.8, -13.67, -13.89, -13.85, -13.99, -14.09, -14.2, -13.82, -14.26, -14.04, -14.9, -15.06, -14.91, -15.3, -15.2, -15.11, -15.58, -15.24, -15.57, -15.75, -16.46], "Spec_H": [-7.77, -7.84, -7.95, -8.03, -8.08, -8.12, -8.07, -8.13, -8.22, -8.2, -8.17, -8.29, -8.37, -8.38, -8.39, -8.51, -8.59, -8.46, -8.62, -9.65, -9.65, -9.64, -9.73, -9.82, -10.21, -10.43, -10.45, -10.49, -10.74, -10.7, -10.77, -10.6, -10.82, -10.66, -10.66, -10.36, -10.44, -10.8, -10.67, -10.89, -10.85, -10.99, -11.09, -11.2, -10.82, -11.26, -11.04, -11.9, -12.06, -11.91, -12.3, -12.2, -12.11, -12.58, -12.24, -12.57, -12.75, -13.46]},
            17: {"Spec_L": [-8.10, -8.21, -8.38, -8.39, -8.39, -8.40, -8.40, -8.46, -8.70, -8.70, -8.66, -8.71, -8.62, -8.60, -8.70, -8.68, -8.84, -8.99, -9.04, -9.16, -9.13, -9.13, -9.31, -9.28, -9.60, -9.72, -9.76, -9.73, -9.94, -9.73, -9.91, -9.68, -9.95, -9.59, -9.76, -10.04, -10.19, -10.20, -10.77, -10.95, -10.47, -10.47, -10.50, -10.28, -10.27, -10.31, -10.34, -11.89, -11.74, -11.35, -12.63, -11.74, -12.37, -12.43, -12.06, -13.12, -11.68, -12.07], "Spec_H": [-6.10, -6.21, -6.38, -6.39, -6.39, -6.40, -6.40, -6.46, -6.70, -6.70, -6.66, -6.71, -6.62, -6.60, -6.70, -6.68, -6.84, -6.99, -7.04, -7.16, -7.13, -7.13, -7.31, -7.28, -7.60, -7.72, -7.76, -7.73, -7.94, -7.73, -7.91, -7.68, -7.95, -7.59, -7.76, -7.04, -7.19, -7.20, -7.77, -7.95, -7.47, -7.47, -7.50, -7.28, -7.27, -7.31, -7.34, -8.59, -8.44, -8.05, -9.33, -8.44, -9.07, -9.13, -8.76, -9.82, -8.38, -8.77]},
            18: {"Spec_L": [-8.57, -8.86, -8.80, -8.60, -8.60, -8.67, -8.79, -8.89, -9.22, -9.21, -9.09, -9.06, -8.94, -8.85, -9.15, -9.04, -9.11, -9.33, -9.21, -9.54, -9.67, -9.75, -9.88, -9.59, -9.90, -10.33, -10.37, -10.22, -10.37, -10.32, -10.39, -10.23, -10.41, -10.06, -10.19, -10.16, -10.17, -10.23, -10.44, -10.76, -10.24, -10.24, -10.37, -10.22, -10.00, -10.13, -10.21, -13.25, -13.39, -12.59, -13.86, -12.94, -13.62, -13.55, -12.79, -13.76, -12.60, -12.86, -14.50, -13.69, -14.43, -13.52, -13.61, -13.49, -13.13, -13.68, -13.54, -14.37, -14.56, -13.92, -13.96, -13.69, -13.89, -14.21, -14.25, -14.32, -14.37, -13.59, -13.24, -13.83, -12.96, -14.37, -13.45, -13.24, -14.13, -12.50, -14.84, -13.74, -14.52, -15.35, -13.65, -14.33, -13.56, -14.73, -15.09, -14.32, -14.43, -14.16], "Spec_H": [-5.57, -5.86, -5.80, -5.60, -5.60, -5.67, -5.79, -5.89, -6.22, -6.21, -6.09, -6.06, -5.94, -5.85, -6.15, -6.04, -6.11, -6.33, -6.21, -6.54, -6.67, -6.75, -6.88, -6.59, -6.90, -7.33, -7.37, -7.22, -7.37, -7.32, -7.39, -7.23, -7.41, -7.06, -7.19, -7.16, -7.17, -7.23, -7.44, -7.76, -7.24, -7.24, -7.37, -7.22, -7.00, -7.13, -7.21, -7.25, -7.39, -6.59, -7.86, -6.94, -7.62, -7.55, -6.79, -7.76, -6.60, -6.86, -8.50, -7.69, -8.43, -7.52, -7.61, -7.49, -7.13, -7.68, -7.54, -8.37, -8.56, -7.92, -7.96, -7.69, -7.89, -8.21, -8.25, -8.32, -8.37, -7.59, -7.24, -7.83, -6.96, -8.37, -7.45, -7.24, -8.13, -6.50, -8.84, -7.74, -8.52, -9.35, -7.65, -8.33, -7.56, -8.73, -9.09, -8.32, -8.43, -8.16]},
            19: {"Spec_L": [-11.97, -12.26, -12.15, -12.48, -12.54, -12.42, -12.25, -12.34, -12.47, -12.61, -12.64, -12.77, -12.67, -12.48, -12.68, -12.65, -12.64, -12.63, -12.79, -13.17, -13.31, -13.39, -13.54, -13.34, -13.65, -14.13, -13.95, -14.12, -14.19, -14.03, -14.08, -14.01, -14.23, -13.94, -14.10, -13.92, -14.08, -14.03, -14.49, -14.57, -14.34, -14.22, -14.40, -14.14, -14.09, -14.33, -14.12, -17.24, -17.02, -16.75, -17.58, -16.90, -16.93, -17.10, -17.18, -17.75, -17.16, -16.96, -18.68, -18.05, -18.70, -17.77, -17.72, -17.37, -17.04, -17.11, -17.46, -18.27, -18.61, -18.21, -17.90, -18.31, -17.70, -18.01, -17.86, -18.11, -18.52, -17.46, -17.99, -17.86, -16.94, -17.89, -16.66, -17.29, -18.02, -16.99, -18.80, -17.52, -18.72, -18.25, -17.55, -18.22, -18.36, -19.41, -19.34, -18.35, -19.38, -19.56], "Spec_H": [-8.97, -9.26, -9.15, -9.48, -9.54, -9.42, -9.25, -9.34, -9.47, -9.61, -9.64, -9.77, -9.67, -9.48, -9.68, -9.65, -9.64, -9.63, -9.79, -10.17, -10.31, -10.39, -10.54, -10.34, -10.65, -11.13, -10.95, -11.12, -11.19, -11.03, -11.08, -11.01, -11.23, -10.94, -11.10, -10.92, -11.08, -11.03, -11.49, -11.57, -11.34, -11.22, -11.40, -11.14, -11.09, -11.33, -11.12, -11.24, -11.02, -10.75, -11.58, -10.90, -10.93, -11.10, -11.18, -11.75, -11.16, -10.96, -12.68, -12.05, -12.70, -11.77, -11.72, -11.37, -11.04, -11.11, -11.46, -12.27, -12.61, -12.21, -11.90, -12.31, -11.70, -12.01, -11.86, -12.11, -12.52, -11.46, -11.99, -11.86, -10.94, -11.89, -10.66, -11.29, -12.02, -10.99, -12.80, -11.52, -12.72, -12.25, -11.55, -12.22, -12.36, -13.41, -13.34, -12.35, -13.38, -13.56]},
            62: {"Spec_L": [-7.52,-7.49,-7.56,-7.61,-7.62,-7.58,-7.53,-7.64,-7.65,-7.63,-7.61,-7.65,-7.65,-7.62,-7.59,-7.65,-7.75,-7.71,-7.71,-7.74,-7.74,-8.08,-8.08,-8,-7.97,-8.05,-8,-8,-8,-8,-8,-8,-8,-8,-8.09,-8.11,-8.13,-8.13,-8.19,-8.19,-8.32,-8.28,-8.32,-8.38,-8.37,-8.4,-8.9,-8.9,-8.9,-8.78,-8.9,-8.9,-8.9,-8.91,-9.07,-9,-9.17,-9.19,-9.16,-9.27,-9.3,-9.21,-9.28,-9.65,-9.65,-9.65,-9.84,-9.57,-9.65,-9.99,-9.94,-9.71,-9.65,-9.94,-9.65,-9.87,-9.88,-10.15,-10.15,-10.15,-10.2,-10.15,-9.87,-10.15,-10.15,-10.15,-10.15,-10.15,-10.15,-10.69,-10.86,-10.99,-10.99,-10.75,-10.85,-11.01,-10.89,-11.27,-11.18,-11.34,-10.86,-11.04,-11.23,-11.22,-11.37,-11.36,-11.52,-11.46,-11.07,-11.36,-11.31,-11.02,-11.19,-11.12,-11.07,-11.31,-11.23,-11.2,-11.17,-11.35,-11.36,-11.28,-11.54,-11.96,-12.07,-12.06,-12.03,-11.96,-12.07], "Spec_H": [-5.52,-5.49,-5.56,-5.61,-5.62,-5.58,-5.53,-5.64,-5.65,-5.63,-5.61,-5.65,-5.65,-5.62,-5.59,-5.65,-5.75,-5.71,-5.71,-5.74,-5.74,-6.08,-6.08,-6,-5.97,-6.05,-6,-6,-6,-6,-6,-6,-6,-6,-6.09,-6.11,-6.13,-6.13,-6.19,-6.19,-6.32,-6.28,-6.32,-6.38,-6.37,-6.4,-5.9,-5.9,-5.9,-5.78,-5.9,-5.9,-5.9,-5.91,-6.07,-6,-6.17,-6.19,-6.16,-6.27,-6.3,-6.21,-6.28,-6.35,-6.35,-6.35,-6.54,-6.27,-6.35,-6.69,-6.64,-6.41,-6.35,-6.64,-6.35,-6.57,-6.58,-6.85,-6.85,-6.85,-6.9,-6.85,-6.57,-6.85,-6.85,-6.85,-6.85,-6.85,-6.85,-5.69,-5.86,-5.99,-5.99,-5.75,-5.85,-6.01,-5.89,-6.27,-6.18,-6.34,-5.86,-6.04,-6.23,-6.22,-6.37,-6.36,-6.52,-6.46,-6.07,-6.36,-6.31,-6.02,-6.19,-6.12,-6.07,-6.31,-6.23,-6.2,-6.17,-6.35,-6.36,-6.28,-6.54,-6.96,-7.07,-7.06,-7.03,-6.96,-7.07]},
            64: {"Spec_L": [-11.92,-11.88,-11.93,-11.98,-12.01,-12.02,-11.97,-12.12,-12.22,-12.22,-12.21,-12.01,-12.23,-12.23,-12.14,-12.15,-12.23,-12.16,-12.24,-12.26,-12.25,-12.74,-12.78,-12.69,-12.74,-12.82,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.79,-12.85,-12.84,-12.82,-12.86,-12.93,-13.08,-13.03,-13.01,-13.07,-13.09,-13.1,-13.6,-13.6,-13.6,-13.62,-13.65,-13.6,-13.6,-13.68,-13.9,-13.85,-14.01,-14.03,-13.99,-14.13,-14.15,-14.12,-14.18,-14.5,-14.5,-14.48,-14.59,-14.43,-14.5,-14.89,-14.85,-14.63,-14.5,-14.9,-14.5,-14.79,-14.79,-15,-15,-15,-15.34,-15,-14.92,-15,-15,-15,-15,-15,-15,-16.37,-16.41,-16.53,-16.56,-16.4,-16.54,-16.63,-16.53,-17.03,-16.87,-17.02,-16.6,-16.81,-16.98,-17,-17.17,-17.09,-17.17,-17.14,-16.81,-17.11,-17.04,-16.77,-16.94,-16.87,-16.81,-17.04,-16.97,-17.05,-17.06,-17.16,-17.16,-17.13,-17.34,-17.8,-18,-17.98,-17.94,-17.95,-18.08], "Spec_H": [-7.92,-7.88,-7.93,-7.98,-8.01,-8.02,-7.96,-8.12,-8.22,-8.22,-8.21,-8.01,-8.23,-8.22,-8.14,-8.15,-8.23,-8.16,-8.24,-8.26,-8.25,-8.74,-8.78,-8.69,-8.74,-8.82,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.79,-8.85,-8.84,-8.82,-8.86,-8.93,-9.08,-9.03,-9.01,-9.07,-9.09,-9.1,-8.6,-8.6,-8.6,-8.62,-8.65,-8.6,-8.6,-8.68,-8.89,-8.85,-9.01,-9.03,-8.99,-9.13,-9.15,-9.12,-9.18,-9.5,-9.5,-9.47,-9.59,-9.43,-9.5,-9.89,-9.85,-9.63,-9.5,-9.9,-9.5,-9.79,-9.79,-10,-10,-10,-10.34,-10,-9.92,-10,-10,-10,-10,-10,-10,-8.37,-8.41,-8.53,-8.55,-8.39,-8.54,-8.63,-8.53,-9.03,-8.87,-9.02,-8.6,-8.81,-8.98,-9,-9.17,-9.1,-9.17,-9.14,-8.81,-9.11,-9.04,-8.78,-8.94,-8.87,-8.81,-9.04,-8.97,-9.05,-9.06,-9.15,-9.16,-9.13,-9.34,-9.8,-10,-9.98,-9.94,-9.96,-10.08]},
        },  # ? 62는 L300 losscal 이라서 SVC와 BtoB Spec이 동일함, 나머지 Type은 다르다.
        "RF_Cable": {
            "N/A": {"Spec_L": [], "Spec_H": []},
            7: {"Spec_L": [-8.78, -8.83, -8.93, -8.95, -8.98, -8.99, -8.96, -9.01, -9.09, -9.05, -9.05, -9.09, -9.12, -9.09, -9.06, -9.1, -9.14, -9.11, -9.25, -9.69, -9.67, -9.63, -9.7, -9.73, -9.82, -9.85, -9.86, -9.91, -10, -9.98, -9.87, -9.87, -9.98, -9.83, -9.87, -10.09, -10.06, -10.21, -10.2, -10.18, -10.4, -10.35, -10.43, -10.25, -10.37, -10.41, -10.54, -10.93, -10.63, -10.78, -10.99, -10.85, -10.84, -10.93, -10.83, -10.92, -11.05, -11.53, -12.73, -12.52, -12.56, -12.49, -12.41, -12.76, -12.33, -12.55, -12.63, -12.6, -12.37, -12.83, -12.92, -13.06, -13.22, -12.83, -12.93, -13.16, -13.3, -13.67, -13.83, -13.42, -13.31, -13.08, -12.7, -13, -12.76, -12.66, -12.86, -12.48, -12.67, -12.82, -12.94, -13.24, -13.26, -13.89, -12.62, -13.19, -13.18, -12.83], "Spec_H": [-5.78, -5.83, -5.93, -5.95, -5.98, -5.99, -5.96, -6.01, -6.09, -6.05, -6.05, -6.09, -6.12, -6.09, -6.06, -6.1, -6.14, -6.11, -6.25, -6.69, -6.67, -6.63, -6.7, -6.73, -6.82, -6.85, -6.86, -6.91, -7, -6.98, -6.87, -6.87, -6.98, -6.83, -6.87, -7.09, -7.06, -7.21, -7.2, -7.18, -7.4, -7.35, -7.43, -7.25, -7.37, -7.41, -7.54, -7.93, -7.63, -7.78, -7.99, -7.85, -7.84, -7.93, -7.83, -7.92, -8.05, -8.53, -6.73, -6.52, -6.56, -6.49, -6.41, -6.76, -6.33, -6.55, -6.63, -6.6, -6.37, -6.83, -6.92, -7.06, -7.22, -6.83, -6.93, -7.16, -7.3, -7.67, -7.83, -7.42, -7.31, -7.08, -6.7, -7, -6.76, -6.66, -6.86, -6.48, -6.67, -6.82, -6.94, -7.24, -7.26, -7.89, -6.62, -7.19, -7.18, -6.83]},
            8: {"Spec_L": [-11.87, -12.22, -12.13, -12.11, -12.14, -12.17, -12.05, -12.09, -12.54, -12.52, -12.54, -12.42, -12.25, -12.29, -12.14, -12.16, -12.35, -12.27, -12.62, -13.43, -13.47, -13.49, -13.55, -13.73, -13.65, -13.67, -13.64, -13.82, -13.86, -13.82, -13.67, -13.71, -13.78, -13.64, -13.83, -14.01, -14.1, -14.15, -14.24, -14.33, -14.24, -14.4, -14.71, -14.48, -14.35, -14.41, -14.68, -15.17, -14.9, -14.86, -15.29, -15.6, -15.42, -15.65, -15.21, -15.28, -15.57, -15.6, -16.38, -16.22, -16.16, -16.11, -15.89, -16.46, -16.19, -16.15, -16.95, -16.89, -16.7, -16.72, -16.66, -16.78, -16.84, -16.56, -16.17, -17.98, -17.97, -17.04, -17.43, -17.44, -17.62, -17.42, -16.89, -16.97, -16.97, -16.83, -17.06, -16.85, -16.72, -16.89, -16.63, -17.28, -17.21, -18.53, -17.11, -16.53, -18.07, -18.04], "Spec_H": [-8.87, -9.22, -9.13, -9.11, -9.14, -9.17, -9.05, -9.09, -9.54, -9.52, -9.54, -9.42, -9.25, -9.29, -9.14, -9.16, -9.35, -9.27, -9.62, -9.43, -9.47, -9.49, -9.55, -9.73, -9.65, -9.67, -9.64, -9.82, -9.86, -9.82, -9.67, -9.71, -9.78, -9.64, -9.83, -10.01, -10.1, -10.15, -10.24, -10.33, -10.24, -10.4, -10.71, -10.48, -10.35, -10.41, -10.68, -11.17, -10.9, -10.86, -11.29, -11.6, -11.42, -11.65, -11.21, -11.28, -11.57, -11.6, -10.38, -10.22, -10.16, -10.11, -9.89, -10.46, -10.19, -10.15, -10.95, -10.89, -10.7, -10.72, -10.66, -10.78, -10.84, -10.56, -10.17, -11.98, -11.97, -11.04, -11.43, -11.44, -11.62, -11.42, -10.89, -10.97, -10.97, -10.83, -11.06, -10.85, -10.72, -10.89, -10.63, -11.28, -11.21, -12.53, -11.11, -10.53, -12.07, -12.04]},
            62: {"Spec_L": [-8.00, -7.97, -8.06, -8.11, -8.12, -8.09, -8.04, -8.16, -8.18, -8.16, -8.14, -8.19, -8.19, -8.16, -8.13, -8.19, -8.30, -8.26, -8.27, -8.31, -8.31, -8.84, -8.84, -8.76, -8.73, -8.81, -8.77, -8.77, -8.77, -8.79, -8.79, -8.79, -8.79, -8.79, -8.90, -8.93, -8.95, -8.96, -9.03, -9.04, -9.19, -9.21, -9.25, -9.32, -9.31, -9.35, -9.36, -9.36, -9.36, -10.25, -10.39, -10.40, -10.50, -10.61, -10.77, -10.71, -10.90, -10.93, -10.91, -11.03, -11.07, -11.00, -11.09, -11.43, -11.45, -11.47, -11.69, -11.42, -11.50, -11.85, -11.82, -11.61, -11.55, -11.85, -11.53, -11.78, -11.80, -12.09, -12.10, -12.12, -12.18, -12.12, -11.83, -12.11, -12.11, -12.10, -12.10, -12.09, -12.08, -11.76, -11.93, -12.07, -12.09, -11.87, -11.98, -12.15, -12.05, -12.63, -12.54, -12.70, -12.22, -12.40, -12.58, -12.51, -12.65, -12.62, -12.77, -12.71, -12.31, -12.59, -12.53, -12.24, -12.41, -12.35, -12.31, -12.55, -12.48, -12.47, -12.51, -12.70, -12.73, -12.67, -13.01, -13.42, -13.46, -13.44, -13.48, -13.53, -13.69], "Spec_H": [-6.00, -5.97, -6.06, -6.11, -6.12, -6.09, -6.04, -6.16, -6.18, -6.16, -6.14, -6.19, -6.19, -6.16, -6.13, -6.19, -6.30, -6.26, -6.27, -6.31, -6.31, -6.84, -6.84, -6.76, -6.73, -6.81, -6.77, -6.77, -6.77, -6.79, -6.79, -6.79, -6.79, -6.79, -6.90, -6.93, -6.95, -6.96, -7.03, -7.04, -7.19, -7.21, -7.25, -7.32, -7.31, -7.35, -7.36, -7.36, -7.36, -6.25, -6.39, -6.40, -6.50, -6.61, -6.77, -6.71, -6.90, -6.93, -6.91, -7.03, -7.07, -7.00, -7.09, -7.43, -7.45, -7.47, -7.69, -7.42, -7.50, -7.85, -7.82, -7.61, -7.55, -7.85, -7.53, -7.78, -7.80, -8.09, -8.10, -8.12, -8.18, -8.12, -7.83, -8.11, -8.11, -8.10, -8.10, -8.09, -8.08, -7.76, -7.93, -8.07, -8.09, -7.87, -7.98, -8.15, -8.05, -8.63, -8.54, -8.70, -8.22, -8.40, -8.58, -8.51, -8.65, -8.62, -8.77, -8.71, -8.31, -8.59, -8.53, -8.24, -8.41, -8.35, -8.31, -8.55, -8.48, -8.47, -8.51, -8.70, -8.73, -8.67, -9.01, -9.42, -9.46, -9.44, -9.48, -9.53, -9.69]},
            64: {"Spec_L": [-11.92,-11.88,-11.93,-11.98,-12.01,-12.02,-11.97,-12.12,-12.22,-12.22,-12.21,-12.01,-12.23,-12.23,-12.14,-12.15,-12.23,-12.16,-12.24,-12.26,-12.25,-12.74,-12.78,-12.69,-12.74,-12.82,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.8,-12.79,-12.85,-12.84,-12.82,-12.86,-12.93,-13.08,-13.03,-13.01,-13.07,-13.09,-13.1,-13.6,-13.6,-13.6,-13.62,-13.65,-13.6,-13.6,-13.68,-13.9,-13.85,-14.01,-14.03,-13.99,-14.13,-14.15,-14.12,-14.18,-14.5,-14.5,-14.48,-14.59,-14.43,-14.5,-14.89,-14.85,-14.63,-14.5,-14.9,-14.5,-14.79,-14.79,-15,-15,-15,-15.34,-15,-14.92,-15,-15,-15,-15,-15,-15,-16.37,-16.41,-16.53,-16.56,-16.4,-16.54,-16.63,-16.53,-17.03,-16.87,-17.02,-16.6,-16.81,-16.98,-17,-17.17,-17.09,-17.17,-17.14,-16.81,-17.11,-17.04,-16.77,-16.94,-16.87,-16.81,-17.04,-16.97,-17.05,-17.06,-17.16,-17.16,-17.13,-17.34,-17.8,-18,-17.98,-17.94,-17.95,-18.08], "Spec_H": [-7.92,-7.88,-7.93,-7.98,-8.01,-8.02,-7.96,-8.12,-8.22,-8.22,-8.21,-8.01,-8.23,-8.22,-8.14,-8.15,-8.23,-8.16,-8.24,-8.26,-8.25,-8.74,-8.78,-8.69,-8.74,-8.82,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.8,-8.79,-8.85,-8.84,-8.82,-8.86,-8.93,-9.08,-9.03,-9.01,-9.07,-9.09,-9.1,-8.6,-8.6,-8.6,-8.62,-8.65,-8.6,-8.6,-8.68,-8.89,-8.85,-9.01,-9.03,-8.99,-9.13,-9.15,-9.12,-9.18,-9.5,-9.5,-9.47,-9.59,-9.43,-9.5,-9.89,-9.85,-9.63,-9.5,-9.9,-9.5,-9.79,-9.79,-10,-10,-10,-10.34,-10,-9.92,-10,-10,-10,-10,-10,-10,-8.37,-8.41,-8.53,-8.55,-8.39,-8.54,-8.63,-8.53,-9.03,-8.87,-9.02,-8.6,-8.81,-8.98,-9,-9.17,-9.1,-9.17,-9.14,-8.81,-9.11,-9.04,-8.78,-8.94,-8.87,-8.81,-9.04,-8.97,-9.05,-9.06,-9.15,-9.16,-9.13,-9.34,-9.8,-10,-9.98,-9.94,-9.96,-10.08]},
        },
    }

    return dict_spec[Type][Current_Type]["Spec_L"], dict_spec[Type][Current_Type]["Spec_H"]

def Type_offset(Type, Current_Type):
    dict_offset = {
        "SVC": {
            16: {"Offset": []},
            17: {"Offset": []},
            18: {"Offset": []},
            19: {"Offset": []},
            62: {"Offset": [-1.06,-1.19,-1.26,-1.21,-1.17,-1.14,-1.17,-1.15,-1.44,-1.50,-1.47,-1.43,-1.39,-1.33,-1.28,-1.32,-1.44,-1.39,-1.42,-1.59,-1.79,-1.72,-1.81,-1.95,-2.07,-1.99,-2.01,-2.04,-2.07,-2.11,-2.15,-2.18,-2.22,-2.25,-2.27,-2.22,-2.50,-2.60,-2.72,-2.71,-2.93,-2.50,-2.94,-2.55,-2.80,-2.84,-2.86,-2.88,-2.90,-2.62,-2.60,-2.57,-2.50,-2.36,-2.67,-3.18,-2.65,-2.66,-2.87,-2.76,-2.35,-2.83,-2.58,-2.94,-2.87,-2.77,-3.60,-2.25,-2.76,-3.27,-2.76,-2.86,-2.99,-3.13,-2.81,-2.54,-4.00,-3.50,-3.30,-3.00,-2.59,-2.85,-3.15,-3.24,-3.34,-3.39,-3.69,-3.89,-4.09,-4.27,-4.09,-3.53,-4.10,-3.50,-3.35,-3.73,-3.99,-3.77,-4.41,-4.72,-3.58,-4.42,-3.88,-2.95,-4.39,-4.25,-3.75,-3.67,-3.83,-3.59,-2.95,-3.19,-4.03,-3.39,-3.33,-4.55,-3.00,-4.41,-4.22,-4.46,-5.08,-4.50,-4.35,-3.39,-4.64,-5.80,-5.08,-4.47,-5.99]},
            64: {"Offset": [-1.06,-1.19,-1.26,-1.21,-1.17,-1.14,-1.17,-1.15,-1.44,-1.50,-1.47,-1.43,-1.39,-1.33,-1.28,-1.32,-1.44,-1.39,-1.42,-1.59,-1.79,-1.72,-1.81,-1.95,-2.07,-1.99,-2.01,-2.04,-2.07,-2.11,-2.15,-2.18,-2.22,-2.25,-2.27,-2.22,-2.50,-2.60,-2.72,-2.71,-2.93,-2.50,-2.94,-2.55,-2.80,-2.84,-2.86,-2.88,-2.90,-2.62,-2.60,-2.57,-2.50,-2.36,-2.67,-3.18,-2.65,-2.66,-2.87,-2.76,-2.35,-2.83,-2.58,-2.94,-2.87,-2.77,-3.60,-2.25,-2.76,-3.27,-2.76,-2.86,-2.99,-3.13,-2.81,-2.54,-4.00,-3.50,-3.30,-3.00,-2.59,-2.85,-3.15,-3.24,-3.34,-3.39,-3.69,-3.89,-4.09,-4.27,-4.09,-3.53,-4.10,-3.50,-3.35,-3.73,-3.99,-3.77,-4.41,-4.72,-3.58,-4.42,-3.88,-2.95,-4.39,-4.25,-3.75,-3.67,-3.83,-3.59,-2.95,-3.19,-4.03,-3.39,-3.33,-4.55,-3.00,-4.41,-4.22,-4.46,-5.08,-4.50,-4.35,-3.39,-4.64,-5.80,-5.08,-4.47,-5.99]},
        },
        "BtoB": {
            16: {"Offset": []},
            17: {"Offset": []},
            18: {"Offset": []},
            19: {"Offset": []},
            62: {"Offset": [-0.35,-0.42,-0.49,-0.39,-0.38,-0.38,-0.4,-0.37,-0.61,-0.65,-0.63,-0.63,-0.64,-0.64,-0.55,-0.5,-0.52,-0.55,-0.71,-0.74,-0.88,-0.61,-0.69,-0.76,-0.83,-0.7,-0.73,-0.76,-0.79,-0.83,-0.87,-0.9,-0.94,-0.97,-1,-1.32,-1.29,-1.25,-1.33,-1.41,-1.38,-1.25,-1.44,-1.12,-1.18,-1.2,-1.22,-1.24,-1.26,-0.96,-0.89,-0.92,-0.95,-1.03,-1.2,-1.58,-1.07,-0.85,-1.01,-0.75,-0.61,-0.79,-0.68,-1.54,-1.57,-1.6,-1.65,-1.23,-1.66,-2.09,-1.52,-1.89,-1.84,-1.8,-1.81,-1.83,-2.2,-1.8,-1.7,-1.6,-1.27,-1.4,-1.54,-1.64,-1.74,-1.79,-2.14,-2.34,-2.54,-2.74,-2.19,-2.45,-2.14,-2.33,-2.02,-2.09,-2.24,-2.46,-2.88,-3.41,-2.45,-2.37,-2.34,-1.56,-2.4,-2.11,-1.75,-2.16,-1.14,-1.27,-1.26,-0.9,-2.02,-1.36,-2.02,-2.36,-1.54,-3.28,-2.36,-3.49,-3.72,-3.23,-2.44,-1.09,-1.99,-4.24,-3.03,-2.12,-2.97]},
            64: {"Offset": [-0.35,-0.42,-0.49,-0.39,-0.38,-0.38,-0.4,-0.37,-0.61,-0.65,-0.63,-0.63,-0.64,-0.64,-0.55,-0.5,-0.52,-0.55,-0.71,-0.74,-0.88,-0.61,-0.69,-0.76,-0.83,-0.7,-0.73,-0.76,-0.79,-0.83,-0.87,-0.9,-0.94,-0.97,-1,-1.32,-1.29,-1.25,-1.33,-1.41,-1.38,-1.25,-1.44,-1.12,-1.18,-1.2,-1.22,-1.24,-1.26,-0.96,-0.89,-0.92,-0.95,-1.03,-1.2,-1.58,-1.07,-0.85,-1.01,-0.75,-0.61,-0.79,-0.68,-1.54,-1.57,-1.6,-1.65,-1.23,-1.66,-2.09,-1.52,-1.89,-1.84,-1.8,-1.81,-1.83,-2.2,-1.8,-1.7,-1.6,-1.27,-1.4,-1.54,-1.64,-1.74,-1.79,-2.14,-2.34,-2.54,-2.74,-2.19,-2.45,-2.14,-2.33,-2.02,-2.09,-2.24,-2.46,-2.88,-3.41,-2.45,-2.37,-2.34,-1.56,-2.4,-2.11,-1.75,-2.16,-1.14,-1.27,-1.26,-0.9,-2.02,-1.36,-2.02,-2.36,-1.54,-3.28,-2.36,-3.49,-3.72,-3.23,-2.44,-1.09,-1.99,-4.24,-3.03,-2.12,-2.97]},
        },  # ? 62는 L300 losscal 이라서 SVC와 BtoB Spec이 동일함, 나머지 Type은 다르다.
        "RF_Cable": {
            "N/A": {"Offset": []},
            7: {"Offset": []},
            8: {"Offset": []},
            62: {"Offset": [-0.48,-0.48,-0.5,-0.5,-0.5,-0.51,-0.51,-0.52,-0.53,-0.53,-0.53,-0.54,-0.54,-0.54,-0.54,-0.54,-0.55,-0.55,-0.56,-0.57,-0.57,-0.76,-0.76,-0.76,-0.76,-0.76,-0.77,-0.77,-0.77,-0.79,-0.79,-0.79,-0.79,-0.79,-0.81,-0.82,-0.82,-0.83,-0.84,-0.85,-0.87,-0.93,-0.93,-0.94,-0.94,-0.95,-0.96,-0.96,-0.96,-0.97,-0.99,-1,-1.1,-1.2,-1.2,-1.21,-1.23,-1.24,-1.25,-1.26,-1.27,-1.29,-1.31,-1.43,-1.45,-1.47,-1.5,-1.5,-1.5,-1.51,-1.53,-1.55,-1.55,-1.56,-1.53,-1.56,-1.57,-1.59,-1.6,-1.62,-1.63,-1.62,-1.61,-1.61,-1.61,-1.6,-1.6,-1.59,-1.58,-1.57,-1.57,-1.58,-1.6,-1.62,-1.63,-1.64,-1.66,-1.86,-1.86,-1.86,-1.86,-1.86,-1.85,-1.79,-1.78,-1.76,-1.75,-1.75,-1.74,-1.73,-1.72,-1.72,-1.72,-1.73,-1.74,-1.74,-1.75,-1.77,-1.84,-1.85,-1.87,-1.89,-1.97,-1.96,-1.89,-1.88,-1.95,-2.07,-2.12]},
            64: {"Offset": [-0.48,-0.48,-0.5,-0.5,-0.5,-0.51,-0.51,-0.52,-0.53,-0.53,-0.53,-0.54,-0.54,-0.54,-0.54,-0.54,-0.55,-0.55,-0.56,-0.57,-0.57,-0.76,-0.76,-0.76,-0.76,-0.76,-0.77,-0.77,-0.77,-0.79,-0.79,-0.79,-0.79,-0.79,-0.81,-0.82,-0.82,-0.83,-0.84,-0.85,-0.87,-0.93,-0.93,-0.94,-0.94,-0.95,-0.96,-0.96,-0.96,-0.97,-0.99,-1,-1.1,-1.2,-1.2,-1.21,-1.23,-1.24,-1.25,-1.26,-1.27,-1.29,-1.31,-1.43,-1.45,-1.47,-1.5,-1.5,-1.5,-1.51,-1.53,-1.55,-1.55,-1.56,-1.53,-1.56,-1.57,-1.59,-1.6,-1.62,-1.63,-1.62,-1.61,-1.61,-1.61,-1.6,-1.6,-1.59,-1.58,-1.57,-1.57,-1.58,-1.6,-1.62,-1.63,-1.64,-1.66,-1.86,-1.86,-1.86,-1.86,-1.86,-1.85,-1.79,-1.78,-1.76,-1.75,-1.75,-1.74,-1.73,-1.72,-1.72,-1.72,-1.73,-1.74,-1.74,-1.75,-1.77,-1.84,-1.85,-1.87,-1.89,-1.97,-1.96,-1.89,-1.88,-1.95,-2.07,-2.12]},
        },
    }

    return dict_offset[Type][Current_Type]["Offset"]


Freq_list_129 = [610, 634, 680, 700, 708, 716, 738, 750, 777, 782, 787, 798, 814, 826, 836, 847, 869, 882, 897, 913, 942, 1430, 1438, 1446, 1462, 1486, 1525, 1542, 1559, 1600, 1620, 1640, 1660, 1695, 1712, 1732, 1751, 1785, 1809, 1852, 1880, 1908, 1922, 1950, 1978, 1995, 2010, 2020, 2025, 2112, 2168, 2185, 2200, 2300, 2350, 2400, 2500, 2535, 2570, 2595, 2620, 2655, 2690, 3300, 3350, 3400, 3425, 3450, 3460, 3475, 3500, 3525, 3540, 3550, 3555, 3575, 3600, 3625, 3650, 3695, 3700, 3750, 3800, 3840, 3850, 3870, 3930, 3950, 3970, 4000, 4030, 4060, 4090, 4120, 4150, 4180, 4200, 4400, 4425, 4450, 4475, 4500, 4525, 4550, 4575, 4600, 4625, 4650, 4675, 4700, 4725, 4750, 4775, 4800, 4825, 4850, 4875, 4900, 4925, 4950, 4975, 5000, 5150, 5300, 5450, 5600, 5750, 5900, 6000]