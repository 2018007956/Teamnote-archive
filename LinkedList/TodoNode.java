class TodoNode {
    Todo value;
    TodoNode prev;
    TodoNode next;

    public Todo getValue() {
        return value;
    }

    public void setValue(Todo value) {
        this.value = value;
    }
}