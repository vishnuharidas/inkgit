A running list of things I've learned — big and small, tech and non-tech.

- **2026-03-07** - Update from GH Mobile App:
    Anthropic named Claude after the American polymath Claude Shannon, who is known as "the father of Information Theory"

- **2026-03-07** — The CSS property `text-wrap: balance` makes headings distribute text more evenly across lines. No JS needed — just one line of CSS:

    ```css
    h1, h2, h3 {
        text-wrap: balance;
    }
    ```

    Supported in all modern browsers since late 2023.

- **2026-03-06** — You can use `git log --oneline --graph --all` to get a nice ASCII art visualization of your branch history right in the terminal.

- **2026-03-05** — In Python, you can unpack a list into **function arguments** with `*`. For example:

    ```python
    def add(a, b, c):
        return a + b + c

    nums = [1, 2, 3]
    print(add(*nums))  # 6
    ```

    Works with `**` for dictionaries too — `func(**{"a": 1, "b": 2})`.

- **2026-03-04** — Honey never spoils. Archaeologists have found [3,000-year-old honey in Egyptian tombs](https://www.smithsonianmag.com/science-nature/the-science-behind-honeys-eternal-shelf-life-1218690/) that was still perfectly edible. Its low moisture, high acidity, and natural hydrogen peroxide make it inhospitable to bacteria.

- **2026-03-03** — The [Voyager 1](https://en.wikipedia.org/wiki/Voyager_1) spacecraft, launched in 1977, is the most distant human-made object — over 24 billion km from Earth. It still communicates with NASA using a 23-watt transmitter, about as powerful as a refrigerator light bulb.

- **2026-03-02** — Sharks are older than trees. Sharks have been around for about [400 million years](https://en.wikipedia.org/wiki/Shark); trees appeared roughly 350 million years ago.

- **2026-03-01** — The word "robot" comes from the Czech word *robota*, meaning forced labor. It was first used in Karel Čapek's [1920 play *R.U.R.*](https://en.wikipedia.org/wiki/R.U.R.) (Rossum's Universal Robots).

- **2026-02-28** — A jiffy is an actual unit of time. In computing, it's the duration of one tick of the system timer interrupt — typically 1 to 10 milliseconds. In physics, it's the time light takes to travel [one centimetre](https://en.wikipedia.org/wiki/Jiffy_(time)) — about 33.4 picoseconds.

- **2026-02-27** — There's a high-altitude lake in Bolivia called [Laguna Colorada](https://en.wikipedia.org/wiki/Laguna_Colorada) that is naturally bright red due to algae and sediment pigments. It's home to thousands of flamingos — and speaking of which, a group of flamingos is called a "flamboyance."

- **2026-02-26** — The `<details>` and `<summary>` HTML elements give you a native collapsible/accordion widget with zero JavaScript:

    ```html
    <details>
        <summary>Click to expand</summary>
        <p>Hidden content here.</p>
    </details>
    ```

    In action:

    <details>
        <summary>Click to expand</summary>
        <p style="color:red">Hidden content here.</p>
    </details>

    Works in all modern browsers and is accessible by default.

- **2026-02-25** — The [Oxford English Dictionary](https://en.wikipedia.org/wiki/Oxford_English_Dictionary) took 70 years to complete (1858–1928). The first editor, Herbert Coleridge, died before reaching the letter C. The current edition has over 600,000 entries.
