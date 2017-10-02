import java.util.Scanner;
public class testprogram
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t=sc.nextInt();
		for(int i=1;i<=t;i++)
		{
			int m = sc.nextInt();
			int n = sc.nextInt();
			int d = m/n;
			System.out.println(d);
			
		}
	}
}
