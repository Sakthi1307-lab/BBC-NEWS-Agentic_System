ROUTER = """Pick the best data source for this question.
- "bbc": a BBC News archive of articles from 2004-2005 (business, entertainment, politics, sport, tech).
- "web": live web search, for anything recent, current, or after 2005.

Question: {question}"""


GRADE = """Does this document help answer the question?

Question: {question}
Document: {document}"""


ANSWER = """Answer the question using ONLY the sources below.
Say which source each fact comes from (BBC archive or the web URL).
If the sources don't contain the answer, say so.

Sources:
{sources}

Question: {question}"""