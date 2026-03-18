with open("index.html", "r") as f:
    content = f.read()

# Find first </section> that closes the correct publications section
# It is followed by orphaned content starting with "<!-- Awards -->" then pub-authors for Healy
start_marker = "</section>\n\n<!-- Awards -->\n            <p class=\"pub-authors\">Healy SA"
# The orphaned block ends with a second </section> followed by the real awards comment
end_marker = "</section>\n\n<!-- Awards -->\n<section id=\"awards\""

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

print(f"start_idx: {start_idx}")
print(f"end_idx: {end_idx}")

if start_idx == -1 or end_idx == -1:
    print("ERROR: markers not found, dumping context around likely location")
    # Print 200 chars around likely area
    idx = content.find("Healy SA, Sagara")
    print(repr(content[max(0,idx-200):idx+200]))
else:
    new_content = (
        content[:start_idx + len("</section>")]
        + "\n\n<!-- Awards -->\n<section id=\"awards\""
        + content[end_idx + len(end_marker):]
    )
    with open("index.html", "w") as f:
        f.write(new_content)
    print("SUCCESS: orphaned block removed")
    print(f"Original length: {len(content)}, New length: {len(new_content)}, Removed: {len(content) - len(new_content)} chars")
