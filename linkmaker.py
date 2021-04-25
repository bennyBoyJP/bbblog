def link_maker(content):

    extract_link = None
    link_name = None
    entry_content_whole = []
    for word in content.split(" "):
        if ">>>" in word:
            link_parts = word.partition(">>>")
            link_name = link_parts[0]
            extract_link = link_parts[-1]
            entry_content_whole.append(link_name)
        else:
            entry_content_whole.append(word)

    entry_content_whole = " ".join(entry_content_whole)

    return entry_content_whole, extract_link, link_name

