import mistune

# Read the Markdown content from a file (assuming "input.md" exists)
with open("input.md", "r") as md_file:
    markdown_content = md_file.read()

# Convert Markdown to plain text
plain_text = mistune.(markdown_content)

# Write the plain text to a file (assuming "output.txt" as the output file)
with open("output.txt", "w") as txt_file:
    txt_file.write(plain_text)

# Print a success message
print("Markdown content successfully converted to plain text and saved as output.txt")

