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
		password = Console.ReadLine();
		Console.WriteLine("Enter conversation uid:");
		threadUid = Console.ReadLine();
		Console.WriteLine("Enter count of messages to read:");
		string tempCount = Console.ReadLine();
		Int32.TryParse(tempCount, out messagesCount);
	}
}