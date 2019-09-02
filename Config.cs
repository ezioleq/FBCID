using System;
using System.IO;

public static class Config{
	public static string contentPath = $"{Environment.CurrentDirectory.ToString()}/content/";
	public static string email, password, threadUid;
	public static int messagesCount;
	
	static Config(){
		if(!Directory.Exists(contentPath))
			Directory.CreateDirectory(contentPath);
	}

	public static void Initlialize(){
		Console.WriteLine("Welcome to Facebook Conversation Image Downloader (FBCID)");
		Console.WriteLine("Enter E-Mail:");
		email = Console.ReadLine();
		Console.WriteLine("Enter password:");
		password = GetPassword();
		Console.WriteLine("\nEnter conversation uid:");
		threadUid = Console.ReadLine();
		Console.WriteLine("Enter count of messages to read:");
		string tempCount = Console.ReadLine();
		Int32.TryParse(tempCount, out messagesCount);
	}

	public static string GetPassword(){
		string password = "";
		ConsoleKeyInfo key;

		do{
			key = Console.ReadKey(true);
			if(key.Key != ConsoleKey.Backspace){
				password += key.KeyChar;
				Console.Write("*");
			}else{
				Console.Write("\b");
			}
		}while(key.Key != ConsoleKey.Enter);
		return password;
	}
}