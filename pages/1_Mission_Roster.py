# pages/1_Mission_Roster.py
# Gated page. check_auth() at the top stops execution here for anyone who has not logged in.

import streamlit as st
from auth import check_auth, show_logout_button
from data_loader import load_astronauts

# Block access immediately if the visitor is not authenticated.
check_auth()

st.set_page_config(page_title="Mission Roster", page_icon="🛰️", layout="wide")

# Show the logout button in the sidebar.
show_logout_button()

st.title("🛰️ Mission Roster")
st.caption(f"Logged in as {st.session_state['username']}")

# Load the astronaut dataset through the cached loader.
astronauts = load_astronauts()

# Build the nationality filter options from the dataset itself, sorted alphabetically.
nationality_options = sorted(astronauts["nationality"].unique())
# Add an "All" option at the front of the list.
nationality_options = ["All"] + nationality_options

# Build the occupation filter options the same way.
occupation_options = sorted(astronauts["occupation"].unique())
occupation_options = ["All"] + occupation_options

# Lay the two filters out side by side.
filter_column_1, filter_column_2 = st.columns(2)

# Add the nationality filter to the first column.
selected_nationality = filter_column_1.selectbox("Nationality", nationality_options)

# Add the occupation filter to the second column.
selected_occupation = filter_column_2.selectbox("Occupation", occupation_options)

# Start with the full dataset, then narrow it down based on the selected filters.
filtered_astronauts = astronauts

# Only filter by nationality if the visitor picked something other than "All".
if selected_nationality != "All":
    filtered_astronauts = filtered_astronauts[filtered_astronauts["nationality"] == selected_nationality]

# Only filter by occupation if the visitor picked something other than "All".
if selected_occupation != "All":
    filtered_astronauts = filtered_astronauts[filtered_astronauts["occupation"] == selected_occupation]

# Count how many rows are left after filtering.
row_count = len(filtered_astronauts)

# Handle the empty-state path, where the filter combination matches no rows.
if row_count == 0:
    st.info("No missions match this filter combination. Try a different nationality or occupation.")
else:
    st.write(f"Showing {row_count} mission record(s).")
    # Show the filtered table. use_container_width=True stretches it to the full column width.
    st.dataframe(
        filtered_astronauts[["name", "nationality", "occupation", "year_of_mission", "mission_title", "hours_mission"]],
        use_container_width=True,
    )
