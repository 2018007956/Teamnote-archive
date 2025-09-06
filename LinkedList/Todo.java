public class Todo {
    private final int id;
    private String task;
    private boolean done;

    public Todo(int id, String title) {
        this.id = id;
        this.task = task;
        this.done = false;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public boolean isDone() {
        return done;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setDone(boolean done) {
        this.done = done;
    }

    @Override
    public String toString() {
        return "[" + id + "] " + title + (done ? " (done)" : "");
    }
}