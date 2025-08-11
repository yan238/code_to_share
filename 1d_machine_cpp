#include <iostream>
using namespace std;

int main() {
    
    cout << "Rules: 30, 90, 110, 54, 184";
    cout << "\nSelect rule: ";
    int rule;
    cin >> rule;

    cout << "Select start: ";
    string start;
    cin >> start;

    int length = start.length();
    bool array[length];
    int counter = 0;
    for (char digit : start) {
        bool in_array;
        if (digit == '0') {
            in_array = false;
        } else if (digit == '1') {
            in_array = true;
        }
        array[counter] = in_array;
        counter++;
    }
    
    cout << "Select runtime: ";
    int runtime;
    cin >> runtime;
    
    while (runtime > 0) {
        cout << "\n";
        cout << "<[";
        for (bool state : array) {
            if (state == false) {
                cout << "░";
            } else if (state == true) {
                cout << "█";
            }
        }
        cout << "]>";
        runtime--;
        
        bool new_array[length];
        copy(array, array + length, new_array);
        int counter = 0;
        for (bool state : array) {
            bool left_state;
            bool right_state;
            
            if (counter == 0) {
                left_state = false;
            } else {
                left_state = array[counter-1];
            }
            if (counter == length-1) {
                right_state = false;
            } else {
                right_state = array[counter+1];
            }
            
            bool new_state = state;
            
            switch(rule) {
                case 30:
                    new_state = left_state ^ (state || right_state);
                    break;
                case 90:
                    new_state = left_state ^ right_state;
                    break;
                case 110:
                    new_state = ((!left_state) && state) || (state ^ right_state) || (left_state && (!right_state));
                    break;
                case 54:
                    new_state = (left_state && !state && !right_state)
                        || (!left_state && state && !right_state)
                        || (!left_state && !state && right_state)
                        || (!left_state && state && right_state);
                    break;
                case 184:
                    new_state = (left_state && state) || (left_state && right_state) || (state && !right_state);
                    break;
            }
            
            new_array[counter] = new_state;
            counter++;
        }
        copy(new_array, new_array + length, array);
    }
}
