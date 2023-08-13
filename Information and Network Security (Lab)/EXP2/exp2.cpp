#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{

    int sqr[6];
    for (int i = 0; i < 6; i++)
    {
        sqr[i] = i * i;
        cout << sqr[i] << "  ";
    }
    cout << endl;

    string inputString;
    cout << "Enter a string: ";
    cin >> inputString;
    int size = inputString.length();

    for (int i = 0; i < 6; i++)
    {
        if (sqr[i] > size)
        {
            size = sqr[i];
            break;
        }
    }
    cout << "size after confirming decimal places " << size << endl;
    size = sqrt(size);

    const int row = size;
    const int col = size;
    char inputArray[row][col];

    int index = 0;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (index < inputString.length())
            {
                inputArray[i][j] = inputString[index];
                index++;
            }
            else
            {
                inputArray[i][j] = '_';
            }
        }
    }

    // cout << "2D Array:" << endl;
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << inputArray[i][j] << " ";
        }
        cout << endl;
    }
    cout << row << endl;
    cout << size << endl;
    int key[row];
    cout << "\nEnter your key now, \nYour key should be less than " << row << " digits ,preciesly in a jumbuled manner but a sequence . \nEnter you key here  " << endl;
    for (int i = 0; i < row; i++)
    {
        cin >> key[i];
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << inputArray[key[i]][j] << " ";
        }
        cout << endl;
    }

    return 0;
}