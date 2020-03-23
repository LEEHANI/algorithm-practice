import java.util.*;

/**
    이름을 어떻게 정렬할건지가 중요한 문제이다.
    이름을 정렬할때 a와 b의 이름 길이가 다르다면 어떻게 할지를 생각했어야 하는 문제..!
    이걸 어떻게 해야할지 몰라서 좀 삽질을 했다. 

    사전순으로 정렬하면 된다..
 */
class Player {
	String name;
	int score;

	Player(String name, int score) {
		this.name = name;
		this.score = score;
	}
}

class Checker implements Comparator<Player> {
  	// complete this method
	public int compare(Player a, Player b) {
        if(a.score > b.score)
        {
            return -1;
        }
        else if(a.score < b.score)
        {
            return 1; 
        }
        else
        {
            if(a.name.equals(b.name))
            {
                return 0;
            }
            else
            {
                int min = a.name.length();
                int answer = -1;

                if(min > b.name.length())
                {
                    min = b.name.length();
                    answer = 1;
                }

                for(int i = 0; i < min ; i ++)
                {
                    int aValue = (int)a.name.charAt(i);
                    int bValue = (int)b.name.charAt(i);

                    if(aValue < bValue)
                    {
                        return -1;
                    }
                    else if(aValue > bValue)
                    {
                        return 1;
                    }
                }

                return answer;
            }
        }
    }
}
