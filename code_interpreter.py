programming_languages = [
    "assembly", "basic", "c", "c++", "cpp", "c#", "cobol", "d", "dart", "elixir", "erlang", "f#","js", "fortran", "go", "groovy", "haskell", "html", "java", "javascript", "julia","kotlin", "lisp", "lua", "matlab", "objective-c", "pascal", "perl", "php", "prolog","python","py", "r", "ruby", "rust", "scala", "scheme", "shell", "smalltalk", "sql","swift", "typescript", "visual basic", "vhdl", "verilog"
]

def generate_code_prompt(topic: str) -> str:
    """
    Enhanced prompt for generating beginner-friendly code examples based on a topic.
    """
    return f"""
    You are a patient, experienced and knowledgeable programming tutor.

    Given the topic below, determine if it relates to programming or computational logic. If so, generate a simple, well-explained code example that demonstrates the concept clearly.

    🛠️ Instructions:
    - Prefer Python, C/C++, Java etc. based on the specific language is mentioned in the topic.
    - The code should be beginner-friendly and easy to follow.
    - Include **clear inline comments** to explain each step.
    - If the topic is theoretical or algorithmic (e.g., recursion, sorting), show a relevant implementation.
    - If the topic is non-coding (e.g., history of Python), briefly state that it doesn't involve code.

    End with a short explanation of what the code does and also display the output of the code.

    🔍 Topic: {topic}
    """