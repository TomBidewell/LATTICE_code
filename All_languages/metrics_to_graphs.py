import csv 
import os
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

# assign directory
directory = '/data/tbidewell/Metrics'
 
# iterate over files in
# that directory
list_of_langs = []

word_lstm_ep_loss_tr = []
word_lstm_ep_loss_dv = []
word_lstm_ep_acc_tr = []
word_lstm_ep_acc_dv = []
word_lstm_test_loss = []
word_lstm_test_acc = []

word_char_lstm_ep_loss_tr = []
word_char_lstm_ep_loss_dv = []
word_char_lstm_ep_acc_tr = []
word_char_lstm_ep_acc_dv = []
word_char_lstm_test_loss = []
word_char_lstm_test_acc = []

transformer_ep_loss_tr = []
transformer_ep_loss_dv = []
transformer_ep_acc_tr = []
transformer_ep_acc_dv = []
transformer_test_loss = []
transformer_test_acc = []


for lang in os.listdir(directory):
    lang_f = os.path.join(directory, lang)
    list_of_langs.append(lang_f.split("/")[-1])

    for model in os.listdir(lang_f):

        model_path = os.path.join(lang_f, model)

        if "w_ch_lstm" in model:
            for file in os.listdir(model_path):
                if "epoch_losses_train.csv" in file:
                    with open(model_path + '/epoch_losses_train.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_char_lstm_ep_loss_tr.append(float(data[-1][0]))
                
                if "epoch_losses_dev.csv" in file:
                    with open(model_path + '/epoch_losses_dev.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_char_lstm_ep_loss_dv.append(float(data[-1][0]))

                if "epoch_accuracy_train.csv" in file:
                    with open(model_path + '/epoch_accuracy_train.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_char_lstm_ep_acc_tr.append(float(data[-1][0]))

                if "epoch_accuracy_dev.csv" in file:
                    with open(model_path + '/epoch_accuracy_dev.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_char_lstm_ep_acc_dv.append(float(data[-1][0]))

                if "test_accuracy_all.csv" in file:
                    with open(model_path + '/test_accuracy_all.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_char_lstm_test_acc.append(float(data[-1][0]))

                if "test_loss_all.csv" in file:
                    with open(model_path + '/test_loss_all.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_char_lstm_test_loss.append(float(data[-1][0]))
        
        if "w_lstm" in model:            
            for file in os.listdir(model_path):
                if "epoch_losses_train.csv" in file:
                    with open(model_path + '/epoch_losses_train.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_lstm_ep_loss_tr.append(float(data[-1][0]))
                
                if "epoch_losses_dev.csv" in file:
                    with open(model_path + '/epoch_losses_dev.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_lstm_ep_loss_dv.append(float(data[-1][0]))

                if "epoch_accuracy_train.csv" in file:
                    with open(model_path + '/epoch_accuracy_train.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_lstm_ep_acc_tr.append(float(data[-1][0]))

                if "epoch_accuracy_dev.csv" in file:
                    with open(model_path + '/epoch_accuracy_dev.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_lstm_ep_acc_dv.append(float(data[-1][0]))

                if "test_accuracy_all.csv" in file:
                    with open(model_path + '/test_accuracy_all.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_lstm_test_acc.append(float(data[-1][0]))

                if "test_loss_all.csv" in file:
                    with open(model_path + '/test_loss_all.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        word_lstm_test_loss.append(float(data[-1][0]))

        if "transformer" in model:            
            for file in os.listdir(model_path):
                if "epoch_losses_train.csv" in file:
                    with open(model_path + '/epoch_losses_train.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        if len(data) != 0:
                            transformer_ep_loss_tr.append(float(data[-1][0]))
                
                if "epoch_losses_dev.csv" in file:
                    with open(model_path + '/epoch_losses_dev.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        if len(data) != 0:
                            transformer_ep_loss_dv.append(float(data[-1][0]))

                if "epoch_accuracy_train.csv" in file:
                    with open(model_path + '/epoch_accuracy_train.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        if len(data) != 0:
                            transformer_ep_acc_tr.append(float(data[-1][0]))

                if "epoch_accuracy_dev.csv" in file:
                    with open(model_path + '/epoch_accuracy_dev.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        if len(data) != 0:
                            transformer_ep_acc_dv.append(float(data[-1][0]))

                if "test_accuracy_all.csv" in file:
                    with open(model_path + '/test_accuracy_all.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        if len(data) != 0:
                            transformer_test_acc.append(float(data[-1][0]))

                if "test_loss_all.csv" in file:
                    with open(model_path + '/test_loss_all.csv', newline='') as f:
                        reader = csv.reader(f)
                        data = list(reader)
                        if len(data) != 0:
                            transformer_test_loss.append(float(data[-1][0]))
            

#word_lstm_ep_loss_tr = word_lstm_ep_loss_tr[:len(word_lstm_ep_loss_tr)-1]


def scatter_plot(df, title):
    fig = px.scatter(df, x= df.columns[1], y=df.columns[2], text='Treebank')

    fig.update_traces(textposition='top center')

    fig.update_layout(
        height=800,
        title_text= title
    )

    fig.show()


def get_df(name_1, list_1, name_2, list_2):
    return pd.DataFrame(list(zip(list_of_langs, list_1, list_2)),
               columns =['Treebank', name_1, name_2])



#scatter_plot(get_df('Transformer', transformer_ep_acc_dv, 'Word_LSTM',  word_lstm_ep_acc_dv), 'Dev Accuracy: transformer vs w_lstm')

#scatter_plot(get_df('Word_Char_LSTM', word_char_lstm_ep_acc_dv, 'Word_LSTM',  word_lstm_ep_acc_dv), 'Dev Accuracy: w_ch_lstm vs w_lstm')

#scatter_plot(get_df('Word_Char_LSTM', word_char_lstm_ep_acc_dv, 'Transformer',  transformer_ep_acc_dv), 'Dev Accuracy: w_ch_lstm vs transformer')

'''
get_df('Transformer', transformer_ep_acc_dv, 'Word_LSTM',  word_lstm_ep_acc_dv).plot(x = 'Transformer', y = 'Word_LSTM', kind = 'scatter')
plt.ylim(0,100)
plt.xlim(0,100)
plt.show()

get_df('Word_Char_LSTM', word_char_lstm_ep_acc_dv, 'Word_LSTM',  word_lstm_ep_acc_dv).plot(x = 'Word_Char_LSTM', y = 'Word_LSTM', kind = 'scatter')
plt.ylim(0,100)
plt.xlim(0,100)
plt.show()

get_df('Word_Char_LSTM', word_char_lstm_ep_acc_dv, 'Transformer',  transformer_ep_acc_dv).plot(x = 'Transformer', y = 'Word_Char_LSTM', kind = 'scatter')
plt.ylim(0,100)
plt.xlim(0,100)
plt.show()


df = get_df('Word_Char_LSTM', word_char_lstm_ep_acc_dv, 'Transformer',  transformer_ep_acc_dv)

df = df[df.Transformer < 50]

print(df.head(10))
'''
'''
get_df('Transformer',  transformer_ep_acc_dv, 'Transformer',  transformer_ep_acc_dv).plot(x = 'Transformer', y = 'Transformer', kind = 'scatter')
plt.ylim(0,100)
plt.xlim(0,100)
plt.show()
'''

df = get_df('Transformer_1',  transformer_ep_acc_dv, 'Transformer',  transformer_ep_acc_dv)

df = df[df.Transformer_1 < 30]

print(df.head(10))