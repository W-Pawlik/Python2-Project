from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "main_theme": "rgb(8,153,147)",
    "section_title": "bold yellow on black",
    "error": "bold red underline",
    "success": "bold green"
})

console = Console(theme=custom_theme)
