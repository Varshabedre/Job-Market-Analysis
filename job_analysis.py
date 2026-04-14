import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("jobs_data.csv")

# Data Cleaning
df = df.drop_duplicates()
df = df.dropna(subset=['Job Title', 'Location', 'Job Description'])

# Skills to check
skills = ['Python', 'SQL', 'Excel', 'Power BI', 'Tableau']

# Extract skills
for skill in skills:
    df[skill] = df['Job Description'].apply(
        lambda x: 1 if skill.lower() in x.lower() else 0
    )

# Skill Demand
skill_counts = df[skills].sum().sort_values(ascending=False)

print("\nMost Demanded Skills:\n", skill_counts)

# Plot Skills
plt.figure()
skill_counts.plot(kind='bar')
plt.title("Most In-Demand Skills")
plt.xticks(rotation=45)
plt.show()

# Location Analysis
top_locations = df['Location'].value_counts().head(10)

print("\nTop Locations:\n", top_locations)

plt.figure()
top_locations.plot(kind='bar')
plt.title("Top Hiring Locations")
plt.xticks(rotation=45)
plt.show()

# Save cleaned data
df.to_csv("cleaned_jobs.csv", index=False)