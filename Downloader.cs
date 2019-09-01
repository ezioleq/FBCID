using fbchat_sharp.API;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

public class Downloader{
	public static async Task Run(){
		Console.WriteLine("Welcome to Facebook Conversation Image Downloader (FBCID)");
		Console.WriteLine("Enter E-Mail:");
		string email = Console.ReadLine();
		Console.WriteLine("Enter password:");
		string password = Console.ReadLine();
		Console.WriteLine("Enter conversation uid:");
		string channelUid = Console.ReadLine();
		Console.WriteLine("Enter count of messages to read:");
		string messagesCount = Console.ReadLine();
		int count;
		Int32.TryParse(messagesCount, out count);

		MessengerClient client = new FBClient();

		await client.DoLogin(email, password, 3);

		var messages = await client.fetchThreadMessages(channelUid, count);

		for(int m = 0; m <= messages.Count-1; m++){
			if(messages[m].attachments.Count > 0){
				for(int a = 0; a <= messages[m].attachments.Count-1; a++){
					string uid = messages[m].attachments[a].uid;
					string url = await client.fetchImageUrl(uid);
					Console.WriteLine(url);
					using(System.Net.WebClient webclient = new System.Net.WebClient()){
						Uri uri = new Uri(url);
						webclient.DownloadFileAsync(uri, $"{Environment.CurrentDirectory.ToString()}/content/{uid}.png");
					}
				}
			}
		}

		await client.doLogout();
		Environment.Exit(0);
	}
}