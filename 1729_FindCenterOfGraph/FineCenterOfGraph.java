
import java.util.Map;

public class FineCenterOfGraph {
    public int findStar_On(int[][] edges){
        int[] degrees = new int[edges.length + 1];
        for (int[] edge : edges){
            degrees[edge[0]]++;
            degrees[edge[1]]++;
        }

        for (int i = 0; i < degrees.length; i++){
            if (degrees[i] == edges.length)
                return i;
        }

        return -1;
    }

    public int findStar_O1(int[][] edges){
        return 
        edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? 
        edges[0][0] : edges[0][1];
    }
}