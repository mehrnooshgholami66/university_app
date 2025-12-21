Console.Write("please select one of opratore\n1: Add\n2: Minus\n3: div\n4: mod\n your oprator : ");
var option = Console.ReadLine();
Console.Write("number 1 : ");
var number1 = float.Parse(Console.ReadLine());
Console.Write("number 2 : ");
var number2 = float.Parse(Console.ReadLine());
switch (option)
{
    case "1":
        Console.WriteLine($"{number1} + {number2} = {number1 + number2}");
        Console.Write("press any key to exit...");
        Console.ReadKey();
        break;
    
    case "2":
        Console.WriteLine($"{number1} - {number2} = {number1 - number2}");
        Console.Write("press any key to exit...");
        Console.ReadKey();
        break;
    
    case "3":
        switch (number2)
        {
            case 0:
                Console.WriteLine("can not divid by zero");
                Console.Write("press any key to exit ... ");
                Console.ReadKey();
            break;
            default:
                Console.WriteLine($"{number1} / {number2} = {number1 / number2}");
                Console.Write("press any key to exit...");
                Console.ReadKey();
                break;
        }
        
        break;
    
    case "4":
        Console.WriteLine($"{number1} % {number2} = {number1 % number2}");
        Console.Write("press any key to exit...");
        Console.ReadKey();
        break;
    
    default: // هیچکدام از کیس ها نباشد
        Console.WriteLine("invalid oprator");
        Console.Write("press any key to exit...");
        Console.ReadKey();
        break;
}