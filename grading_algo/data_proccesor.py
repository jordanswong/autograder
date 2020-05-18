import pandas as pd
from grading_algo import data_prep

'upload dataset'
tr_raw_data = pd.read_excel("data/training_set_rel3.xlsx")
tr_raw_data = tr_raw_data[tr_raw_data.essay_set <= 4]

'cut uneeded data from datasets'
tr_cut_data = tr_raw_data[['essay_id', 'essay_set', 'essay', 'domain1_score']]


'create new processed/ simplified dataset'
'admittedly, it greatly simplifies the dataset/ scoring - makes it easier for this project'
tr_simp_data = pd.DataFrame()

'slice the raw training data only into the parts we need'
tr_cut_data = tr_raw_data[['essay_id', 'essay_set', 'essay', 'domain1_score']]

'apply functions to columns of dataset, and put them into new dataframe of processed data (tr_simp_data)'
tr_simp_data['sent_count'] = tr_cut_data['essay'].apply(data_prep.num_sents)
print('counted sentences')
tr_simp_data['word_count'] = tr_cut_data['essay'].apply(data_prep.num_words)
print('counted words')
tr_simp_data['avg_sent_length'] = tr_cut_data['essay'].apply(data_prep.avg_sent)
print('found average sentence length')
tr_simp_data['grade'] = tr_cut_data.apply(lambda x: data_prep.grade(x['essay_set'], x['domain1_score']), axis=1)
print('calculated grades')

'output this data to a csv file'
tr_simp_data.to_csv('essay_train.csv', index=False, encoding='utf-8')

