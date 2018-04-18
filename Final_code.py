import pickle
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import codecs
from sklearn.metrics import classification_report
def create_feature_file(rname,wname,feat):
    f = codecs.open(rname, encoding = "latin")
    data = f.read()
    #data = data[:2]
    train_data =  data.split("\n\n")
    
    train = []
    label = []
    for i in range(len(train_data)):
        if(len(train_data[i])==0):
            continue
        lis = train_data[i].split("\n")
        seq = []
        lab = []
    
        #print(len(lis),lis,i)
        for word in lis:
            #print(word)
            seq.append(word.split()[0])
            lab.append(word.split()[1])
            #print("seq = ",lab)
        train.append(seq)
        label.append(lab)
    print("Seprated")
    
    #ADD POS Feature    
    if "1" in feat:
        
        pickle_in = open(rname[:-4]+"_POS.pickle","rb")
        POS = pickle.load(pickle_in)
        pickle_in.close()   
               
        print("POS")
    
    #ADD Synonym feature
    if "2" in feat:
        pickle_in = open(rname[:-4]+"_SYN.pickle","rb")
        SYN = pickle.load(pickle_in)
        pickle_in.close() 
        print("SYN")
    
    #ADD Glove Word Embedding as feature
    if "3" in feat:
        pickle_in = open(rname[:-4]+"_GE.pickle","rb")
        GE = pickle.load(pickle_in)
        pickle_in.close() 
        
        print("GE")
    
    #ADD MH & MN categories Feature
    if "4" in feat:
        pickle_in = open(rname[:-4]+"_MH.pickle","rb")
        MH_MN = pickle.load(pickle_in)
        pickle_in.close() 
        print("MH")  
    
    if "5" in feat:
        pickle_in = open(rname[:-4]+"_Ortho.pickle","rb")
        Ortho = pickle.load(pickle_in)
        pickle_in.close() 
        print("Ortho")  
    
    if "6" in feat:
        pickle_in = open(rname[:-4]+"_Stem.pickle","rb")
        Stem = pickle.load(pickle_in)
        pickle_in.close() 
        print("Stem")  
    
    train_feature = ""
    for i,sen in enumerate(train):
        st = ""
        for j,word in enumerate(sen):
            st = st + word + " "
            if "5" in feat:
                st = st + Ortho[i][j] + " "
            if "6" in feat:
                st = st + Stem[i][j] + " "
            if "1" in feat:
                st = st + POS[i][j] + " "
            if "2" in feat:
                if SYN[i][j]!="UNKNOWN":
                    st = st + SYN[i][j] + " "
            if "3" in feat:
                st = st + GE[i][j]
                
            if "4" in feat:
                st = st + MH_MN[i][j] + " "
            
            st = st + label[i][j] + "\n"
        train_feature = train_feature + st + "\n"
        
    f = open(wname,"w")
    f.write(train_feature)
    f.close()
    
feat = ["1","2","3","4","6"]
create_feature_file("training.txt","train_feature.txt",feat)
create_feature_file("dev.txt","dev_feature.txt",feat)
create_feature_file("test.txt","test_feature.txt",feat)

