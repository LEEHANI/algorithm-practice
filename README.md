# backjoon-online-judge
코딩테스트 준비


## Java  
입출력 시 Scanner, Sysout대신 BReader, BWriter를 쓰자  
+ Scanner, System.out.println  
```  
Scanner scan = new Scanner(System.int);

int n = scan.nextInt();

scan.nextLine();

String str = scan.nextLine();
```  

+ BufferedReader, BuffredWriter  
```  
BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

try
{
    int n = Integer.parseInt(bf.readLine());
    String str = bf.readLine();

    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write(n + "\n");
    bw.write(str + "\n");

    bw.flush(); // 남아있는 데이터 모두 출력
    bw.close(); // 스트림 닫기

}
catch(Exception e)
{
	// TODO: handle exception
}
```  
