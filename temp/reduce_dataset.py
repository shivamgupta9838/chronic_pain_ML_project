import pandas as pd

# Load dataset
df = pd.read_csv("all_watch_data_4hz.csv")

# Randomly select 480 rows per person_id
new_df = df.groupby("person_id", group_keys=False).apply(
    lambda x: x.sample(n=min(480, len(x)), random_state=42)
).reset_index(drop=True)

# Save new dataset
new_df.to_csv("cropped_dataset.csv", index=False)

print("New dataset saved as cropped_dataset.csv")
print(new_df["person_id"].value_counts().sort_index())