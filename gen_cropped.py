from pathlib import Path
import random

dirs = "Curated", "PSI 0.5", "PSI 1.0", "Real"
pathss = {name: random.sample(list(Path(name).iterdir()), 100) for name in dirs}


print("""
<html>
<head>
    <style>
        body {
            margin: 0;
        }
        .choices {
            flex-direction: row;
            justify-content: center;
            align-items: center;
            display: flex;
            min-width: 1800px;
        }
        .choice-name {
            width: 100%;
            text-align: center;
            visibility: hidden;
            margin: 0;
            font-size: 4em;
        }
        .choices:active .choice-name {
            visibility: visible;
        }
        .choice-img-shift {
            margin-top: -50px;
        }
        .choice-img-wrapper {
            width: 450px;
            height: 600px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
    <script>
        window.onload = function() {
            function observe(elems) {
                for (elem of elems) {
                    if (elem.isIntersecting) {
                        elem.target.setAttribute("src", elem.target.getAttribute("data-src"));
                    }
                }
            }
            const imageObserver = new IntersectionObserver(observe, {"threshold": 0});
            for (elem of document.getElementsByClassName("choice-img")) {
                console.log(elem);
                imageObserver.observe(elem);
            }
        }
    </script>
</head>
<body>
""")
for _ in range(100):
    puzzle = [(kind, paths.pop()) for kind, paths in pathss.items()]
    random.shuffle(puzzle)

    print("""    <div class="choices">""")
    img = """\
        <div class="choice">
            <div class="choice-img-wrapper"><div class="choice-img-shift">
                <img class="choice-img" data-src="{path}" width="1024" height="1024" />
            </div></div>
            <p class="choice-name">{choice}</p>
        </div>"""
    for choice, path in puzzle:
        print(img.format(choice=choice, path=path))
    print("    </div>")
print("""
</body>
</html>
""")