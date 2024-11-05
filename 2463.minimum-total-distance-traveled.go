/*
 * @lc app=leetcode id=2463 lang=golang
 *
 * [2463] Minimum Total Distance Traveled
 */

// @lc code=start
// MinFloat function to return the minimum of two float64 values
func MinFloat(a, b float64) float64 {
	if a < b {
		return a
	}
	return b
}

// Abs function to return the absolute value of an integer
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func minimumTotalDistance(robot []int, factory [][]int) int64 {
	// Sort the factories and robots
	sort.Slice(factory, func(i, j int) bool {
		return factory[i][0] < factory[j][0]
	})
	sort.Ints(robot)

	// Unpack the factory slice into expanded factories based on capacity
	var factories []int
	for _, f := range factory {
		position := f[0]
		capacity := f[1]
		for i := 0; i < capacity; i++ {
			factories = append(factories, position)
		}
	}

	n := len(robot)
	m := len(factories)

	// Initialize DP Table with positive infinity
	dp := make([][]float64, n+1)
	for i := range dp {
		dp[i] = make([]float64, m+1)
		for j := range dp[i] {
			dp[i][j] = math.Inf(1)
		}
	}

	// Base case: no robots, zero distance
	for j := 0; j <= m; j++ {
		dp[0][j] = 0
	}

	// Fill DP table
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			dp[i][j] = MinFloat(dp[i][j-1], dp[i-1][j-1]+float64(Abs(robot[i-1]-factories[j-1])))
		}
	}
	// fmt.Println(dp)

	// Return the minimum distance for all robots visiting all factories, converted to int64
	return int64(dp[n][m])
}

// @lc code=end
