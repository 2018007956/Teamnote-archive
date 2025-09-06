import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class TodoService {

    private TodoNode head;
    private TodoNode tail;
    private int idSeq = 1;

    // CREATE: 맨 뒤에 추가
    public Todo create(String task) {
        Todo todo = new Todo(idSeq++, task);
        TodoNode node = new TodoNode(todo);

        if (head == null) {
            head = tail = node;
        } else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        return todo;
    }

    // READ: id로 조회
    public Optional<Todo> get(int id) {
        TodoNode n = findNode(id);
        return n == null ? Optional.empty() : Optional.of(n.value);
    }

    // READ: 전체 목록
    public List<Todo> list() {
        List<Todo> result = new ArrayList<>();
        TodoNode cur = head;
        while (cur != null) {
            result.add(cur.value);
            cur = cur.next;
        }
        return result;
    }

    // UPDATE: 제목/완료여부 변경
    public void update(int id, String newTask, Boolean done) {
        Node current = head;
        while (current != null) {
            if (current.id == id) {
                current.task = newTask;
                current.done = done;
                System.out.println("Updated: " + id + " -> " + newTask + " | " + done);
                return;
            }
            current = current.next;
        }
        throw new IllegalArgumentException("Task with id " + id + " not found.");
    }

    // DELETE
    public void delete(int id) {
        TodoNode n = findNode(id);
        if (n == null) throw new IllegalArgumentException("Task with id " + id + " not found.");

        // 연결 끊기
        if (n.prev != null) n.prev.next = n.next; else head = n.next;
        if (n.next != null) n.next.prev = n.prev; else tail = n.prev;

        // 가비지 컬렉션 유도
        n.prev = n.next = null;
        n.value = null;
    }

    public int size() {
        int cnt = 0;
        for (TodoNode cur = head; cur != null; cur = cur.next) cnt++;
        return cnt;
    }

    private TodoNode findNode(int id) {
        TodoNode cur = head;
        while (cur != null) {
            if (cur.value.getId() == id) {
                return cur;
            }
            cur = cur.next;
        }
        return null;
    }
}
