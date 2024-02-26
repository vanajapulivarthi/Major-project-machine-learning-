
from django.shortcuts import render
import joblib

def Home(request):
    return render(request,'Predict_home.html')

def result(request):
    model1 = joblib.load('static/models/thyroid_model')
    model2 = joblib.load('static/models/pcos_model')
    model3 = joblib.load('static/models/liver_model')

    if(request.GET['sex'] != ""):
        sex = int(request.GET['sex'])
        on_thyroxine = int(request.GET['on thyroxine'])
        query_hypothyroid = int(request.GET['query hypothyroid'])
        tSH_measured = int(request.GET['tSH measured'])
        tSH = int(request.GET['tSH'])
        t3 = int(request.GET['t3'])
        tt4_measured = int(request.GET['tt4 measured'])
        tt4 = int(request.GET['tt4'])
        t4U = int(request.GET['t4U'])
        ftI = int(request.GET['ftI'])

        x_test = [[sex, on_thyroxine, query_hypothyroid, tSH_measured, tSH, t3, tt4_measured, tt4, t4U, ftI]]
        y_pred = model1.predict(x_test)
        if y_pred[0] == 0:
            y_pred_t = " Person has no Thyroid "
        else:
            y_pred_t = " Person has Thyroid "
    if(request.GET['sex'] == ""):
        y_pred_t = ""

    if(request.GET['BMI'] != ""):
        BMI = int(request.GET['BMI'])
        I_beta_HCG = int(request.GET['  I   beta-HCG(mIU/mL)'])
        TSH = int(request.GET['TSH (mIU/L)'])
        AMH = int(request.GET['AMH(ng/mL)'])
        Weight_gain = int(request.GET['Weight gain(Y/N)'])
        hair_growth = int(request.GET['hair growth(Y/N)'])
        Skin_darkening = int(request.GET['Skin darkening (Y/N)'])
        Follicle_No_L = int(request.GET['Follicle No. (L)'])
        Follicle_No_R = int(request.GET['Follicle No. (R)'])


        x_test = [[BMI, I_beta_HCG, TSH, AMH, Weight_gain, hair_growth, Skin_darkening, Follicle_No_L, Follicle_No_R]]
        y_pred = model2.predict(x_test)

        if y_pred[0] == 0:
            y_pred_p = " Person has no PCOS "
        else:
            y_pred_p = " Person has PCOS "
    if (request.GET['BMI'] == ""):
        y_pred_p = ""

    if (request.GET['Age'] != ""):
        Age = int(request.GET['Age'])
        Gender = int(request.GET['Gender'])
        TotalBilirubin = int(request.GET['TotalBilirubin'])
        DirectBilirubin = int(request.GET['DirectBilirubin'])
        AlkphosAlkalinePhosphotase = int(request.GET['AlkphosAlkalinePhosphotase'])
        SgptAlamineAminotransferase = int(request.GET['SgptAlamineAminotransferase'])
        SgotAspartateAminotransferase = int(request.GET['SgotAspartateAminotransferase'])
        TotalProtiens = int(request.GET['TotalProtiens'])
        ALBAlbumin = int(request.GET['ALBAlbumin'])
        AGRatioAlbuminandGlobulin_Ratio = int(request.GET['A/GRatioAlbuminandGlobulin Ratio'])

        x_test = [[Age, Gender, TotalBilirubin, DirectBilirubin, AlkphosAlkalinePhosphotase, SgptAlamineAminotransferase,
             SgotAspartateAminotransferase, TotalProtiens, ALBAlbumin, AGRatioAlbuminandGlobulin_Ratio]]
        y_pred = model3.predict(x_test)
        if y_pred[0] == 1:
            y_pred_l = " Person has Liver Disease "
        else:
            y_pred_l = " Person has No Liver Disease "

    if (request.GET['Age'] == ""):
        y_pred_l = ""

    if(y_pred_t != ""):
        if(y_pred_p != "" or y_pred_l!=""):
            if(y_pred_p!=""):
                if(y_pred_l!=""):
                    final_pred = "Person has Thyroid, PCOS and Liver Disease"
                else:
                    final_pred = "Person has Thyroid and PCOS"
            else:
                if (y_pred_l != ""):
                    final_pred = "Person has Thyroid and Liver Disease"
                else:
                    final_pred = y_pred_t
        else:
            final_pred = y_pred_t
    else:
        if (y_pred_p != ""):
            if (y_pred_l != ""):
                final_pred = "Person has PCOS and Liver Disease"
            else:
                final_pred = y_pred_p

        else:
            if (y_pred_l != ""):
                final_pred = y_pred_l
            else:
                final_pred = ""







    return render(request, 'predict_result.html', {'result': final_pred})

