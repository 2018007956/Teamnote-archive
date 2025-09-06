import java.util.List;

public class TodoController {
    public static void main(String[] args) {
        TodoService svc = new TodoService();

        // CREATE
        svc.create("운동하기");
        svc.create("알고리즘 풀이");
        svc.create("장보기");

        // LIST
        print(svc.list());

        // UPDATE (제목만)
        svc.update(2, "알고리즘 풀이 - DFS/BFS", null);
        // UPDATE (완료 플래그만)
        svc.update(1, null, true);

        print(svc.list());

        // GET
        svc.get(2).ifPresent(t -> System.out.println("조회: " + t));

        // DELETE
        System.out.println("삭제(3): " + svc.delete(3));
        System.out.println("삭제(99): " + svc.delete(99));

        print(svc.list());

        System.out.println("현재 개수: " + svc.size());
    }

    private static void print(List<Todo> todos) {
        System.out.println("==== TODOS ====");
        for (Todo t : todos) {
            System.out.println(t);
        }
        System.out.println("===============");
    }
}
