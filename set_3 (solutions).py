def relationship_status(from_member, to_member, social_graph):
    """
    Determine the relationship status between two members in a social graph.
    
    Relationship status can be:
    - "follower" if from_member follows to_member
    - "followed by" if from_member is followed by to_member
    - "friends" if both follow each other
    - "no relationship" if neither follows the other
    
    Args:
        from_member (str): The subject member username (with @)
        to_member (str): The object member username (with @)
        social_graph (dict): Dictionary containing relationship data
        
    Returns:
        str: The relationship status between the members
    """
    # Check if from_member exists in the social graph
    if from_member not in social_graph:
        return "no relationship"
    
    # Check if to_member exists in the social graph
    if to_member not in social_graph:
        return "no relationship"
    
    # Check if from_member follows to_member
    follows_to = to_member in social_graph[from_member]["following"]
    
    # Check if to_member follows from_member
    followed_by = from_member in social_graph[to_member]["following"]
    
    # Determine relationship status
    if follows_to and followed_by:
        return "friends"
    elif follows_to:
        return "follower"
    elif followed_by:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    """
    Evaluate a tic-tac-toe board and determine the winner.
    
    Checks rows, columns, and diagonals for any player having a complete line.
    The board can be of any square size (3x3, 4x4, etc.).
    
    Args:
        board (list): A square list of lists representing the board
        
    Returns:
        str: The symbol of the winner or "NO WINNER" if there is no winner
    """
    size = len(board)
    
    # Check rows for a winner
    for row in board:
        # Skip empty rows or rows with empty cells
        if '' in row:
            continue
            
        # If all elements in the row are the same, we have a winner
        if all(cell == row[0] for cell in row):
            return row[0]
    
    # Check columns for a winner
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        
        # Skip columns with empty cells
        if '' in column:
            continue
            
        # If all elements in the column are the same, we have a winner
        if all(cell == column[0] for cell in column):
            return column[0]
    
    # Check main diagonal (top-left to bottom-right)
    diagonal1 = [board[i][i] for i in range(size)]
    if '' not in diagonal1 and all(cell == diagonal1[0] for cell in diagonal1):
        return diagonal1[0]
    
    # Check other diagonal (top-right to bottom-left)
    diagonal2 = [board[i][size-1-i] for i in range(size)]
    if '' not in diagonal2 and all(cell == diagonal2[0] for cell in diagonal2):
        return diagonal2[0]
    
    # If no winner was found
    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    """
    Calculate the estimated travel time between two stops on a circular route.
    
    The route is one-way and fully connected. This function determines
    the time required to travel from first_stop to second_stop.
    
    Args:
        first_stop (str): The starting stop
        second_stop (str): The destination stop
        route_map (dict): Dictionary with travel times between stops
        
    Returns:
        int: The time in minutes to travel from first_stop to second_stop
    """
    # If both stops are the same, the travel time is 0
    if first_stop == second_stop:
        return 0
    
    # Get all unique stops from the route map
    all_stops = set()
    for leg in route_map:
        all_stops.add(leg[0])
        all_stops.add(leg[1])
    
    # Initialize variables
    current_stop = first_stop
    total_time = 0
    visited = set()
    
    # Travel the route until we reach the second stop
    while current_stop != second_stop:
        # Mark current stop as visited to avoid infinite loops
        visited.add(current_stop)
        
        # Find the next stop in the route
        next_stop = None
        for leg in route_map:
            if leg[0] == current_stop:
                next_stop = leg[1]
                total_time += route_map[leg]["travel_time_mins"]
                break
        
        # If no next stop was found or we've visited all stops without finding second_stop
        if next_stop is None or next_stop in visited:
            # This shouldn't happen in a valid circular route
            return -1
        
        current_stop = next_stop
    
    return total_time
