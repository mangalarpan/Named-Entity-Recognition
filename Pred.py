import codecs
from sklearn.metrics import classification_report
f = codecs.open("dev_feature.txt",encoding = "latin")
data = f.read().split("\n")
true_label = []
for i in range(len(data)):
    if(len(data[i]))>0:
        true_label.append(data[i][-1])
f = codecs.open("dev_out.txt",encoding = "latin")
data = f.read().split("\n")
pred_label = []
for i in range(len(data)):
    if(len(data[i]))>0:
        pred_label.append(data[i][0])
    
print(classification_report(true_label,pred_label))

f = codecs.open("test_feature.txt",encoding = "latin")
data = f.read().split("\n")
true_label = []
for i in range(len(data)):
    if(len(data[i]))>0:
        true_label.append(data[i][-1])
f = codecs.open("test_out.txt",encoding = "latin")
data = f.read().split("\n")
pred_label = []
for i in range(len(data)):
    if(len(data[i]))>0:
        pred_label.append(data[i][0])
    
print(classification_report(true_label,pred_label))
    
