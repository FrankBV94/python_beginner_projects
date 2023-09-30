function generate_solution(self, grid) {
		/* generates a full solution with backtracking */
		number_list = [1,2,3,4,5,6,7,8,9];
		for (i in range(0,81)) {
			row=i//9;
			col=i%9;
			#find next empty cell;
			if (grid[row][col]==0) {
				shuffle(number_list)      
				for (number in number_list) {
					if (self.valid_location(grid,row,col,number)) {
						self.path.push((number,row,col));
						grid[row][col]=number;
						if (!self.find_empty_square(grid)) {
							return true;
						} else {
							if (self.generate_solution(grid)) {
								#if (the grid === full;
								return true;
				break;
		grid[row][col]=0  
		return falsealse;
							}
						}

					}

				}

			}

		}

}

