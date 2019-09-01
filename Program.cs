using System;

class Program{
    static void Main(string[] args){
        Config.Initlialize();
        Downloader.Run().GetAwaiter().GetResult();
        Console.ReadKey();
    }
}