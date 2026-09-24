# pages/2_Astronaut_Lookup.py
# Second gated page, reusing the same check_auth() guard as Mission Roster.

import streamlit as st
from auth import check_auth, show_logout_button
from data_loader import load_astronauts

# Block access immediately if the visitor is not authenticated.
check_auth()

st.set_page_config(page_title="Astronaut Lookup", page_icon="🔎", layout="wide")

# Show the logout button in the sidebar.
show_logout_button()

st.title("🔎 Astronaut Lookup")
st.caption(f"Logged in as {st.session_state['username']}")

# Load the astronaut dataset through the same cached loader used by Mission Roster.
astronauts = load_astronauts()

# Let the visitor search by last name.
search_text = st.text_input("Search by name (e.g. \"Glenn\")")

# Only run a search once the visitor has typed something.
if search_text != "":
    # case=False makes the match case-insensitive; na=False treats missing names as no match.
    matches = astronauts[astronauts["name"].str.contains(search_text, case=False, na=False)]

    # Count how many rows matched.
    match_count = len(matches)

    # Handle the empty-state path, where the search text matches no astronaut.
    if match_count == 0:
        st.info(f'No astronaut found matching "{search_text}".')
    else:
        st.write(f"Found {match_count} matching mission record(s).")
        st.dataframe(
            matches[["name", "nationality", "occupation", "year_of_mission", "mission_title", "hours_mission", "eva_hrs_mission"]],
            use_container_width=True,
        )
else:
    st.write("Enter a name above to look up an astronaut's mission history.")
