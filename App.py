import plotly.express as px
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import plotly.graph_objects as go
import numpy as np
import os

st.set_page_config(layout="wide")
# Fixing Hebrew text orientation
matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.titlepad'] = 20

st.logo("data:image/png;base64,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")

grouped_data = os.path.join(os.path.dirname(__file__), 'grouped_data.csv')
g = pd.read_csv(grouped_data)

# Aggregating data by Quarter and PoliceDistrict
aggregated_data = g.groupby(['Quarter', 'PoliceDistrict'], as_index=False).sum()

grouped_data_by_cluster = os.path.join(os.path.dirname(__file__), 'grouped_data_by_cluster.csv')
data = pd.read_csv(grouped_data_by_cluster)

preprocessed_data = os.path.join(os.path.dirname(__file__), 'preprocessed_data.csv')
df = pd.read_csv(preprocessed_data)

st.markdown("""<style>
        html {
            direction: RTL;
            text-align: right;
        }
        h1, h2, h3, h4, h5 {
            text-align: right;
        }
    </style>""", unsafe_allow_html=True)

# Custom CSS to set text direction to right-to-left
st.markdown(
    """
    <style>
    .rtl-text {
        direction: rtl;
        text-align: right;
    }
    .inline-buttons {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="rtl-text">חקירת מגמות שונות בהיקף הפשיעה בישראל</h1>', unsafe_allow_html=True)
st.markdown('''
<h3 class="rtl-text">
בדאשבורד זה אנו מתמקדים בניתוח מגמות הפשיעה בישראל על פני תקופות זמן שונות ובאזורים גיאוגרפיים מגוונים. מטרת הדאשבורד היא להבין כיצד היקף הפשיעה משתנה במרוצת השנים ובחלוקה למחוזות ולמרחבי המשטרה השונים, לחקור את הקשר בין הפשיעה לבין אשכולות חברתיים-כלכליים ורמת דתיות הישוב.
באמצעות דאשבורד זה, ניתן לזהות תבניות ודפוסים בהתפלגות העבירות, ולהשוות בין האזורים השונים בארץ.
</h3>
''', unsafe_allow_html=True)
st.markdown('''
<div class="rtl-text">
בחר את מחוז המשטרה:
</div>
''', unsafe_allow_html=True)


color_sequence_district = ['#a65628', '#74c476', '#ff7f00', '#f768a1', '#e5d8bd', '#e41a1c', '#fec44f']

# Create the figure for all districts
fig_all_districts = px.line(
    aggregated_data, x='Quarter', y='TikimSum', color='PoliceDistrict',
    title="מגמות התיקים שנפתחו לפי מחוז משטרה",
    color_discrete_sequence=color_sequence_district,
    hover_data={'Quarter': True, 'TikimSum': ':.3s'}
)
fig_all_districts.update_layout(
    yaxis_title=dict(
        text="כמות התיקים", standoff=100,
        font=dict(size=20)  # Increase the text size
    ), xaxis_title=dict(
        text="רבעון",
        font=dict(size=20)  # Increase the text size
    ), title_x=0.75, legend_title=dict(
        text="מחוז משטרה",
        font=dict(size=20)  # Increase the text size
    ),
    hoverlabel=dict(font_size=20),
    legend=dict(font=dict(size=18))
)

fig_all_districts.add_vline(x=9, line=dict(dash='dash', color='white'), annotation_text='סגר ראשון', annotation_position='top')
fig_all_districts.add_vline(x=11, line=dict(dash='dash', color='white'), annotation_text='סגר שני', annotation_position='top')
fig_all_districts.add_vline(x=12, line=dict(dash='dash', color='white'), annotation_text='סגר שלישי', annotation_position='top')
fig_all_districts.add_vline(x=13, line=dict(dash='dash', color='white'), annotation_text='שומר החומות', annotation_position='top')
fig_all_districts.add_vline(x=6, line=dict(dash='dash', color='white'), annotation_text='מחאת יוצאי אתיופיה-סלומון טקה', annotation_position='top')


fig_all_districts.for_each_yaxis(lambda yaxis: yaxis.update(tickfont=dict(size=15)))
fig_all_districts.for_each_xaxis(lambda xaxis: xaxis.update(tickfont=dict(size=15)))
fig_all_districts.update_traces(
    hovertemplate='%{x}<br>סכום התיקים=%{y:,}'
)

# Dropdown with an additional "כלל המחוזות" option
options = ["כלל המחוזות"] + list(g['PoliceDistrict'].unique())
selected_district = st.selectbox("", options, label_visibility="hidden")
if selected_district == "כלל המחוזות":
    st.plotly_chart(fig_all_districts)
else:
    district_data = g[g['PoliceDistrict'] == selected_district]
    
    # Aggregate data by Quarter to get the total TikimSum for each quarter
    quarter_totals = district_data.groupby('Quarter')['TikimSum'].sum().reset_index()
    quarter_totals.rename(columns={'TikimSum': 'TotalTikimSum'}, inplace=True)
    
    # Merge the total TikimSum with the district data
    district_data = pd.merge(district_data, quarter_totals, on='Quarter', how='left')
    
    fig = px.line(
        district_data, x='Quarter', y='TikimSum', color='PoliceMerhav',
        title=f'מגמות התיקים שנפתחו ב{selected_district}',
        color_discrete_sequence=color_sequence_district,
        hover_data={'Quarter': True, 'TikimSum': ':.3s', 'TotalTikimSum': True}
    )
    fig.update_layout(
        yaxis_title=dict(
            text="כמות התיקים", standoff=100,
            font=dict(size=20)  # Increase the text size
        ), xaxis_title=dict(
            text="רבעון",
            font=dict(size=20)  # Increase the text size
        ), title_x=0.75, legend_title=dict(
            text="מרחב",
            font=dict(size=20)  # Increase the text size
        ), hoverlabel=dict(font_size=20),
        legend=dict(font=dict(size=15))
    )
    fig.add_vline(x=9, line=dict(dash='dash', color='white'), annotation_text='סגר ראשון', annotation_position='top')
    fig.add_vline(x=11, line=dict(dash='dash', color='white'), annotation_text='סגר שני', annotation_position='top')
    fig.add_vline(x=12, line=dict(dash='dash', color='white'), annotation_text='סגר שלישי', annotation_position='top')
    fig.add_vline(x=13, line=dict(dash='dash', color='white'), annotation_text='שומר החומות', annotation_position='top')
    fig.add_vline(x=6, line=dict(dash='dash', color='white'), annotation_text='מחאת יוצאי אתיופיה-סלומון טקה', annotation_position='top')
    fig.for_each_yaxis(lambda yaxis: yaxis.update(tickfont=dict(size=15)))
    fig.for_each_xaxis(lambda xaxis: xaxis.update(tickfont=dict(size=15)))
    fig.update_traces(
        hovertemplate='%{x}<br>סכום התיקים=%{y:,}<br>סכום התיקים הכולל במחוז=%{customdata[0]:,}'
    )
    st.plotly_chart(fig)

# Assuming 'data' is your DataFrame
all_crime_groups = data['StatisticCrimeGroup'].unique()

selected_groups = st.multiselect("בחר את קבוצות הפשיעה", all_crime_groups, default=all_crime_groups, label_visibility="hidden")

# Filter data based on selected groups
filtered_data = data[data['StatisticCrimeGroup'].isin(selected_groups)] if selected_groups else pd.DataFrame(columns=data.columns)

# Create the figure
if not filtered_data.empty:
    fig = px.histogram(filtered_data, x='Cluster', y='norm', color='StatisticCrimeGroup', barmode='stack',
                       title=f'התפלגות העבירות הנ"ל לפי האשכול החברתי-כלכלי של היישוב', hover_data={'Cluster': False, 'StatisticCrimeGroup': True, 'norm':':.3s'})
else:
    # Create an empty figure with the same layout
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[], y=[]))
    fig.update_layout(title=f'התפלגות העבירות הנ"ל לפי האשכול החברתי-כלכלי של היישוב')
fig.for_each_yaxis(lambda yaxis: yaxis.update(tickfont=dict(size=15)))
fig.for_each_xaxis(lambda xaxis: xaxis.update(tickfont=dict(size=15)))
fig.update_xaxes(tickmode='linear', tick0=1, dtick=1)
fig.update_layout(barmode='relative', bargap=0.2, xaxis_title=dict(
        text="אשכול כלכלי-חברתי",
        font=dict(size=20)  # Increase the text size
    ), yaxis_title=dict(
        text="סכום התיקים המנורמל בגודל האוכלוסייה", standoff=100,
        font=dict(size=20)  # Increase the text size
    ),
                  legend_title=dict(
        text="קבוצת העבירות",
        font=dict(size=20)  # Increase the text size
    ), title_x=0.7, height=650,hoverlabel=dict(font_size=20),
    legend=dict(font=dict(size=15)))
fig.update_traces(
    hovertemplate='קבוצת העבירה=%{fullData.name}<br>סכום התיקים המנורמל=%{y:,}'
)
if len(selected_groups) == 1:
        fig.update_layout(showlegend=False)

st.plotly_chart(fig)

# Convert 'Quarter' to 'Year' for further analysis
df['Year'] = df['Quarter'].str[:4].astype(int)
data['Year'] = data['Quarter'].str[:4].astype(int)

# Prompt the user to select a crime group in Hebrew
st.markdown('''
<h5 class="rtl-text">
בחר את קבוצת העבירה:
</h5>
''', unsafe_allow_html=True)

# Function to plot relative crime by religion and group
def plot_relative_crime_by_religion_and_group(df, data, selected_group):
    # Merge the two dataframes on StatisticCrimeGroup, Cluster, and Year
    merged_df = pd.merge(df, data, on=['StatisticCrimeGroup', 'Year'], suffixes=('_original', '_norm'))
    # Ensure Year is treated as a categorical variable with a specific order
    merged_df['Year'] = pd.Categorical(merged_df['Year'], ordered=True, categories=sorted(df['Year'].unique()))
    
    # Set the order of the 'Religious level' column and use blue color saturation levels
    desired_order = ['חילונים', 'מסורתיים', 'דתיים', 'חרדים']
    merged_df['Religious level'] = pd.Categorical(merged_df['Religious level'], categories=desired_order, ordered=True)

    # Define color sequence with varying saturation levels of blue
    color_sequence = [ '#cc4c02', '#ec7014', '#fe9929', '#fee391']

    # If 'כלל העבירות' is selected, compute relative crime for all crime groups
    if selected_group == 'כלל העבירות':
        # Compute the total number of crimes for each crime group and year
        total_crimes_per_group = merged_df.groupby(['StatisticCrimeGroup', 'Year'])['TikimSum_original'].sum().reset_index()
        total_crimes_per_group.columns = ['StatisticCrimeGroup', 'Year', 'TotalTikimSum']
        # Merge the total crimes with the merged dataframe
        df_merged = pd.merge(merged_df, total_crimes_per_group, on=['StatisticCrimeGroup', 'Year'])
        # Compute the relative number of crimes for each religious level within each crime group
        df_merged['RelativeTikimSum'] = df_merged['TikimSum_original'] / df_merged['TotalTikimSum']
        # Group by crime group, religious level, and year
        relative_crime_data = df_merged.groupby(['StatisticCrimeGroup', 'Religious level', 'Year']).agg({'RelativeTikimSum': 'sum',
            'TikimSum_original': 'sum'}).reset_index()
        # Plot the relative bar chart with small multiples for each year
        fig = px.bar(relative_crime_data, x='RelativeTikimSum', y='StatisticCrimeGroup', color='Religious level',
                     title=f'הקשר בין רמת הדתיות לרמת הפשיעה לפי קבוצת עבירה',
                     labels={'StatisticCrimeGroup': 'קבוצת עבירה', 'RelativeTikimSum': 'חלק הפשיעה היחסי', 'Religious level': 'רמת דתיות', 'TikimSum_original': 'כמות התיקים'},
                     barmode='stack',  # Use stacked bar mode
                     hover_data={'StatisticCrimeGroup': False, 'Year': False, 'Religious level': False, 'TikimSum_original': True, 'RelativeTikimSum': True},
                     facet_col='Year',
                     color_discrete_sequence=color_sequence,
                     category_orders={'Year': sorted(unique_years), 'Religious level': desired_order},
                     facet_col_wrap=6,
                     height=700,  # Set the height to fit the page
                     facet_row_spacing=0.05)  # Adjust row spacing if needed
    else:
        # Filter the dataframe by selected crime group
        filtered_df = merged_df[merged_df['StatisticCrimeGroup'] == selected_group]
        # Compute the total number of crimes for each crime type and year within the selected crime group
        total_crimes_per_type = filtered_df.groupby(['StatisticCrimeType', 'Year'])['TikimSum_original'].sum().reset_index()
        total_crimes_per_type.columns = ['StatisticCrimeType', 'Year', 'TotalTikimSum']
        # Merge the total crimes with the filtered dataframe
        df_merged = pd.merge(filtered_df, total_crimes_per_type, on=['StatisticCrimeType', 'Year'])
        # Compute the relative number of crimes for each religious level within each crime type
        df_merged['RelativeTikimSum'] = df_merged['TikimSum_original'] / df_merged['TotalTikimSum']
        # Group by crime type, religious level, and year
        relative_crime_data = df_merged.groupby(['StatisticCrimeType', 'Religious level', 'Year']).agg({'RelativeTikimSum': 'sum',
            'TikimSum_original': 'sum'}).reset_index()
        # Plot the relative bar chart with small multiples for each year
        fig = px.bar(relative_crime_data, x='RelativeTikimSum', y='StatisticCrimeType', color='Religious level',
                     title=f'הקשר בין מידת הדתיות של היישוב לרמת הפשיעה לפי {selected_group}',
                     labels={'StatisticCrimeType': 'עבירה', 'RelativeTikimSum': 'חלק הפשיעה היחסי', 'Religious level': 'רמת דתיות', 'TikimSum_original': 'כמות התיקים'},
                     barmode='stack',  # Use stacked bar mode
                     hover_data={'StatisticCrimeType': False, 'Year': False, 'Religious level': False, 'TikimSum_original': True, 'RelativeTikimSum': True},
                     facet_col='Year',
                     color_discrete_sequence=color_sequence,
                     category_orders={'Year': sorted(unique_years), 'Religious level': desired_order},
                     facet_col_wrap=6,
                     height=700,  # Set the height to fit the page
                     facet_row_spacing=0.05)  # Adjust row spacing if needed

    # Update layout to show x-axis in all facets
    fig.for_each_yaxis(lambda yaxis: yaxis.update(tickfont=dict(size=15, color="white")))
    fig.for_each_xaxis(lambda xaxis: xaxis.update(tickfont=dict(size=15, color="white")))

    # Update layout of the bar chart
    fig.update_layout(title_x=0.65, hoverlabel=dict(font=dict(size=18, color="white")),
                      legend=dict(font=dict(size=15, color="white")),
                      legend_title=dict(font=dict(size=15, color="white")),
                      yaxis_title=dict(
                          font=dict(size=20, color="white"),  # Increase the text size
                          standoff=200
                      ),
                      yaxis=dict(
                          autorange='reversed'  # Reverse the y-axis order
                      ))

    # Display the bar chart
    st.plotly_chart(fig, use_container_width=True)

# Display a disclaimer in Hebrew
st.markdown('''
<h5 class="rtl-text">
בגרף זה המציגים אינם מנסים להעליל ביצוע עבירות על קבוצות מסוימות מהאוכלוסיה. הסיווג הוא ברמת היישוב, לפי נתוני הלמס
</h5>
''', unsafe_allow_html=True)

# Get unique years from the dataframe
unique_years = df['Year'].unique()

# Add a dropdown to select the crime group
crime_groups = sorted(['כלל העבירות'] + df['StatisticCrimeGroup'].unique().tolist())
selected_group = st.selectbox('', crime_groups)

# Call the function to plot the chart
plot_relative_crime_by_religion_and_group(df, data, selected_group)
