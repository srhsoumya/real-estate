from flask import Flask,render_template,request
import numpy as np
import pickle
model=pickle.load(open('final_model_pickle.pickle','rb'))
locations=["bath", "bhk", "area", " Devarachikkanahalli", "1st Block Jayanagar", "1st Phase JP Nagar", "2nd Phase Judicial Layout", "2nd Stage Nagarbhavi", "5th Phase JP Nagar", "6th Phase JP Nagar", "7th Phase JP Nagar", "8th Phase JP Nagar", "9th Phase JP Nagar", "AECS Layout", "Abbigere", "Akshaya Nagar", "Ambalipura", "Ambedkar Nagar", "Amruthahalli", "Anandapura", "Ananth Nagar", "Anekal", "Anjanapura", "Ardendale", "Arekere", "Attibele", "BEML Layout", "BTM 2nd Stage", "BTM Layout", "Babusapalaya", "Badavala Nagar", "Balagere", "Banashankari", "Banashankari Stage II", "Banashankari Stage III", "Banashankari Stage V", "Banashankari Stage VI", "Banaswadi", "Banjara Layout", "Bannerghatta", "Bannerghatta Road", "Basavangudi", "Basaveshwara Nagar", "Battarahalli", "Begur", "Begur Road", "Bellandur", "Benson Town", "Bharathi Nagar", "Bhoganhalli", "Billekahalli", "Binny Pete", "Bisuvanahalli", "Bommanahalli", "Bommasandra", "Bommasandra Industrial Area", "Bommenahalli", "Brookefield", "Budigere", "CV Raman Nagar", "Chamrajpet", "Chandapura", "Channasandra", "Chikka Tirupathi", "Chikkabanavar", "Chikkalasandra", "Choodasandra", "Cooke Town", "Cox Town", "Cunningham Road", "Dasanapura", "Dasarahalli", "Devanahalli", "Dodda Nekkundi", "Doddaballapur", "Doddakallasandra", "Doddathoguru", "Domlur", "Dommasandra", "EPIP Zone", "Electronic City", "Electronic City Phase II", "Electronics City Phase 1", "Frazer Town", "GM Palaya", "Garudachar Palya", "Giri Nagar", "Gollarapalya Hosahalli", "Gottigere", "Green Glen Layout", "Gubbalala", "Gunjur", "HBR Layout", "HRBR Layout", "HSR Layout", "Haralur Road", "Harlur", "Hebbal", "Hebbal Kempapura", "Hegde Nagar", "Hennur", "Hennur Road", "Hoodi", "Horamavu Agara", "Horamavu Banaswadi", "Hormavu", "Hosa Road", "Hosakerehalli", "Hoskote", "Hosur Road", "Hulimavu", "ISRO Layout", "ITPL", "Iblur Village", "Indira Nagar", "JP Nagar", "Jakkur", "Jalahalli", "Jalahalli East", "Jigani", "Judicial Layout", "KR Puram", "Kadubeesanahalli", "Kadugodi", "Kaggadasapura", "Kaggalipura", "Kaikondrahalli", "Kalena Agrahara", "Kalyan nagar", "Kambipura", "Kammanahalli", "Kammasandra", "Kanakapura", "Kanakpura Road", "Kannamangala", "Karuna Nagar", "Kasavanhalli", "Kasturi Nagar", "Kathriguppe", "Kaval Byrasandra", "Kenchenahalli", "Kengeri", "Kengeri Satellite Town", "Kereguddadahalli", "Kodichikkanahalli", "Kodigehaali", "Kodihalli", "Kogilu", "Konanakunte", "Koramangala", "Kothannur", "Kothanur", "Kudlu", "Kudlu Gate", "Kumaraswami Layout", "Kundalahalli", "LB Shastri Nagar", "Laggere", "Lakshminarayana Pura", "Lingadheeranahalli", "Magadi Road", "Mahadevpura", "Mahalakshmi Layout", "Mallasandra", "Malleshpalya", "Malleshwaram", "Marathahalli", "Margondanahalli", "Marsur", "Mico Layout", "Munnekollal", "Murugeshpalya", "Mysore Road", "NGR Layout", "NRI Layout", "Nagarbhavi", "Nagasandra", "Nagavara", "Nagavarapalya", "Narayanapura", "Neeladri Nagar", "OMBR Layout", "Old Airport Road", "Old Madras Road", "Padmanabhanagar", "Pai Layout", "Panathur", "Parappana Agrahara", "Pattandur Agrahara", "Poorna Pragna Layout", "Prithvi Layout", "R.T. Nagar", "Rachenahalli", "Raja Rajeshwari Nagar", "Rajaji Nagar", "Rajiv Nagar", "Ramagondanahalli", "Ramamurthy Nagar", "Rayasandra", "Sahakara Nagar", "Sanjay nagar", "Sarakki Nagar", "Sarjapur", "Sarjapur  Road", "Sarjapura - Attibele Road", "Sector 2 HSR Layout", "Sector 7 HSR Layout", "Seegehalli", "Shampura", "Shivaji Nagar", "Singasandra", "Somasundara Palya", "Sompura", "Sonnenahalli", "Subramanyapura", "Sultan Palaya", "TC Palaya", "Talaghattapura", "Thanisandra", "Thigalarapalya", "Thubarahalli", "Thyagaraja Nagar", "Tindlu", "Tumkur Road", "Ulsoor", "Uttarahalli", "Varthur", "Varthur Road", "Vasanthapura", "Vidyaranyapura", "Vijayanagar", "Vishveshwarya Layout", "Vishwapriya Layout", "Vittasandra", "Whitefield", "Yelachenahalli", "Yelahanka", "Yelahanka New Town", "Yelenahalli", "Yeshwanthpur"]

def final_model (bath,bhk,area,location):
    p=np.zeros(240)
    p[0]=bath
    p[1]=bhk
    p[2]=area
    for i in range(3,239):
        if locations[i]==location:
            p[i]=1
            print(i)
    return model.predict([p])

app=Flask(__name__)
@app.route('/')
def home():

    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    bath=request.form["bath"]
    bhk=request.form["bhk"]
    area=request.form["area"]
    locat=request.form["locat"]
    return render_template('index.html',pre_text="predicted amount in lakhs :{}".format(str((final_model(bath,bhk,area,locat)[0]))))


if __name__=='__main__':
    app.run(debug=True)
