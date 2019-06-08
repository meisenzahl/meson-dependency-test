#include <gtest/gtest.h>

#include "shape.hpp"

TEST(shape, Constructor)
{
    shape s();
}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}
