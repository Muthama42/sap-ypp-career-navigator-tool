def recommend_certificates(keywords, certificates_df):
    matches = []
    for kw in keywords:
        matches.extend(certificates_df[certificates_df.apply(lambda row: kw.lower() in str(row).lower(), axis=1)].to_dict('records'))
    # Remove duplicates
    seen = set()
    unique_matches = []
    for m in matches:
        t = tuple(m.items())
        if t not in seen:
            unique_matches.append(m)
            seen.add(t)
    return unique_matches 