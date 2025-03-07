context("read_micro_region")

# skip tests because they take too much time
skip_if(Sys.getenv("TEST_ONE") != "")
testthat::skip_on_cran()


test_that("read_micro_region", {

  # read data
  expect_true(is(  read_micro_region(code_micro="AC") , "sf"))
  expect_true(is(  read_micro_region(code_micro="AC", year=2010) , "sf"))
  # expect_true(is(  read_micro_region(code_micro=11, year=2010) , "sf"))
  expect_true(is(  read_micro_region(code_micro="all", year=2010)  , "sf"))

  # check filter
  test_filter <-  read_micro_region(code_micro=11008, year=2010)
  expect_equal( nrow(test_filter), 1)

})



# ERRORS
test_that("read_micro_region", {

  expect_error(read_micro_region(code_micro=9999999, year=9999999))

  # Wrong code
  expect_error(read_micro_region(code_micro=9999999))
  expect_error(read_micro_region(code_micro=5201108312313213))

  # Wrong year
  expect_error(read_micro_region( year=9999999))

})
