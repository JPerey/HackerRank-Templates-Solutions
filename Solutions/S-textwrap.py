import textwrap

def wrap(string, max_width):
    
    new_string = textwrap.wrap(string, max_width)
    final_string = "\n".join(new_string)
    return final_string