def route_query(state):

    query = state["user_query"].lower()

    if "captain" in query:
        return "team"

    elif "runs" in query or "strike rate" in query:
        return "batting"

    elif "wickets" in query or "economy" in query:
        return "bowling"

    elif "venue" in query or "pitch" in query:
        return "venue"

    elif "form" in query:
        return "form"

    elif "vs" in query:
        return "h2h"

    else:
        return "records"