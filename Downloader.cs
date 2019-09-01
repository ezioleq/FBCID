using fbchat_sharp.API;
using System;
using System.Threading.Tasks;

public class Downloader{
	public static async Task Run(){
		MessengerClient client = new FBClient();
		await client.DoLogin(Config.email, Config.password, 3);

		var messages = await client.fetchThreadMessages(Config.threadUid, Config.messagesCount);

		for(int m = 0; m <= messages.Count-1; m++){
			if(messages[m].attachments.Count > 0){
				for(int a = 0; a <= messages[m].attachments.Count-1; a++){
					string uid = messages[m].attachments[a].uid;
					string url = await client.fetchImageUrl(uid);
					Console.WriteLine(url);
					using(System.Net.WebClient webclient = new System.Net.WebClient()){
						webclient.DownloadFileAsync(new Uri(url), $"{Config.contentPath}/{uid}.png");
					}
				}
			}
		}

		await client.doLogout();
		Environment.Exit(0);
	}
}