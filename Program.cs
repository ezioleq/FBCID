using System;
using System.Threading;
using System.Threading.Tasks;

class Program{
    static void Main(string[] args){
        Downloader.Run().GetAwaiter().GetResult();
        Console.ReadKey();
    }
}