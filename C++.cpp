#include <iostream>

int main() {
    int x = 100;

    // Lambda 1：不捕获任何外部变量，只接收两个参数 a, b
    auto add = [](int a, int b) {
        std::cout << "[add] a = " << a << ", b = " << b << "\n";
        // std::cout << x; // ❌ 错误！不能访问 x
        return a + b;
    };

    // Lambda 2：捕获 x 的值（拷贝），可以访问但不能修改 x
    auto add_with_x_copy = [x](int a) {
        std::cout << "[add_with_x_copy] a = " << a << ", x = " << x << "\n";
        return a + x;
    };

    // Lambda 3：捕获 x 的引用，可以访问并修改 x
    auto add_with_x_ref = [&x](int a) {
        x += a;
        std::cout << "[add_with_x_ref] a = " << a << ", modified x = " << x << "\n";
        return x;
    };

    // 调用
    std::cout << "add(3, 4) = " << add(3, 4) << "\n\n";
    std::cout << "add_with_x_copy(5) = " << add_with_x_copy(5) << "\n";
    std::cout << "[main] x after add_with_x_copy = " << x << "\n\n";

    std::cout << "add_with_x_ref(7) = " << add_with_x_ref(7) << "\n";
    std::cout << "[main] x after add_with_x_ref = " << x << "\n";

    return 0;
}
