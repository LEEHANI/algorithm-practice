import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * 배열을 shift해야한다고 나머지 전부를 해야하는 건 아니다..
 * 이 문제의 경우 shift가 발생하더라도 3번만 발생함
 */
public class NewYearChaos {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // int a[] = {2,1,5,3,4};
        // int a[] = {5,1,2,3,7,8,6,4};
        // minimumBribes(a);

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }

            minimumBribes(q);
        }

        scanner.close();
    }

    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        int temp[] = new int[q.length];
        int answer = 0;

        for(int j = 0; j < q.length; j++){
            temp[j] = j+1;
        }

        for(int i = 0; i < q.length; i++)
        {
            if(temp[i]==q[i])
            {
                continue;
            }

            if(i+1 < q.length && temp[i+1]==q[i])
            {
                temp[i+1] = temp[i];
                answer ++;
            }
            else if(i+2 < q.length && temp[i+2] == q[i])
            {
                temp[i+2] = temp[i+1];
                temp[i+1] = temp[i];
                answer +=2;
            } else
            {
                answer = -1;
                break;
            }
        }

        if(answer > 0)
        {
            System.out.println(answer);
        }
        else
        {
            System.out.println("Too chaotic");
        }
    }

    static void minimumBribes1(int[] q) {
        int answer = 0;

        Deque<Integer> l = new LinkedList<>();
        
        for(int i = q.length-1; i >= 0 ; i--)
        {
            int index = i+1;
            int flag = 0;

            if(q[i] == index)
            {
                continue;
            }
            
            System.out.println(index + " " + l);

            if(!l.isEmpty())
            {
                if(l.size()==2 && l.getLast() == index)
                {
                    answer+=1;
                    l.remove(l.getLast());
                    flag = 1;
                }
                else if(l.size() <= 2 && l.peek() == index)
                {
                    l.poll();
                    flag = 1;
                }
                else if(l.size()>2)
                {
                    answer = -1;
                    break;    
                }
            }

            if(q[i] > -1)
                l.add(q[i]);

            if(flag==0 && (i-1) >= 0 && index == q[i-1] )
            {
                q[i-1] = -1;
                answer +=1;
            }
            else if(flag==0 && (i-2) >= 0 && index == q[i-2])
            {
                q[i-2] = -1;
                answer +=2;                
            }
            else if(flag==0)
            {
                answer = -1;
                break;
            }
        }

        System.out.println();
        System.out.println(answer);
        System.out.println(l.size());
        System.out.println(l.peek());

        if(answer > 0 && l.isEmpty())
        {
            System.out.println(answer);
        }
        else
        {
            System.out.println("Too chaotic");
        }
    }
}