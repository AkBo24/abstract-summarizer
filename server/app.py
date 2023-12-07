from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from todo import todos
from scholarly_util import query
from open_ai_util import summarize_abstract

app = Flask(__name__)
limiter = Limiter(
    get_remote_address, 
    app=app,
    storage_uri="memory://",
)

assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
js = Bundle("src/*.js", output="dist/main.js") # new

assets.register("css", css)
css.build()

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
@limiter.limit('5/minute')
def search_todo():
    search_query = request.form.get("search")
    if not search_query:
        return '<p>Empty search query</p>'

    query_res = query(search_query)
    return render_template("journal.html", records=query_res['records'])

    # search_term = request.form.get("search")

    # if not len(search_term):
    #     return render_template("todo.html", todos=[])

    # res_todos = []
    # for todo in todos:
    #     if search_term in todo["title"]:
    #         res_todos.append(todo)

    # return render_template("todo.html", todos=res_todos)

@app.route("/summarize", methods=["POST"])
def summarize_openai():
    abstract = request.form.get("abstract")
    openai_summary = summarize_abstract(abstract=abstract)

    print(openai_summary.usage.total_tokens)

    return f'<p>{openai_summary.choices[0].message.content}</p>'

if __name__ == "__main__":
    app.run(debug=True)