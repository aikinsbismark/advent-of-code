#include <fstream>
#include <iostream>
#include <string>


int main() {
    std::ifstream input_file("../input/2025-1");

    if (!input_file.is_open()) {
        std::cerr << "Failed to open" << "\n";
        return 1;
    }

    std::string rotation{};
    int dial_position = 50;
    int total_zeros = 0;

    while(getline(input_file, rotation)) {
        char direction = rotation[0];
        int distance = std::stoi(rotation.substr(1));

        if (direction == 'L') {
            dial_position -= distance;
        }
        else {
            dial_position += distance;
        }

        dial_position = (dial_position % 100 + 100) % 100;

        if (dial_position == 0) {
            total_zeros += 1;
        }
    }
    std::cout << "Total zeros: " << total_zeros << "\n";

    return 0;
}