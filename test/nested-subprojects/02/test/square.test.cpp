#include <gtest/gtest.h>

#include "square.hpp"

TEST(square, Constructor)
{
    square s();
}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}
