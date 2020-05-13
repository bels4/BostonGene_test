##### using ComBat

# taking samples data
samples_data = list(expression_dataframe.columns)[2:]

# finding out cancer subtype for each sample
samples_subtype = [annotation_table.loc[annotation_table.icgc_id == sample].subtype.values[0] for sample in samples_data]

# creating batch list with class numbers to create batches for ComBat
subtype_data = [subtype_sample[sample] for sample in samples_subtype]

# taking naked our dataframe to use combat on it
df_before_combat = expression_dataframe.drop(columns=['gene_name', 'gene_id'])

# some magic for columns names -_-
df_before_combat.columns = [i for i in range(96)]

# using ComBat
df_after_combat = combat.combat(df_before_combat, subtype_data)

# deleting
del df_before_combat