import java.util.*;
import java.io.*;
//Node class
class Node
{
    int data;
    Node left;
    Node right;
    Node(int key)
    {
        data = key;
        left = null;
        right = null;
    }
}
public class BinaryTree
{
    static Node insert(Node root, int key)
    {
        Node temp = new Node(key);
        Queue<Node> q = new LinkedList<Node>();
        if(root==null)
        {
            root = temp;
        }
        else
        {
            q.add(root);
            while(!q.isEmpty())
            {
                Node cur = q.peek();
                q.remove();
                if(cur.left==null)
                {
                    cur.left = temp;
                    break;
                }else
                    q.add(cur.left);
                if(cur.right==null)
                {
                    cur.right = temp;
                    break;
                }else
                    q.add(cur.right);
            }
        }
        return root;
    }
    static void inorder(Node root)
    {
        if(root!=null)
        {
            inorder(root.left);
            System.out.print(root.data+" ");
            inorder(root.right);
        }
    }
    static void preorder(Node root)
    {
        if(root!=null)
        {
            System.out.print(root.data+" ");
            preorder(root.left);
            preorder(root.right);
        }
    }
    static void postorder(Node root)
    {
        if(root!=null)
        {
            postorder(root.left);
            postorder(root.right);
            System.out.print(root.data+" ");
        }
    }
    static void levelorder(Node root)
    {
        if(root==null)
            return;
        Queue<Node> q1 = new LinkedList<Node>();
        q1.add(root);
        while(!q1.isEmpty())
        {
            Node cur = q1.poll();
            System.out.print(cur.data+" ");
            if(cur.left!=null)
                q1.add(cur.left);
            if(cur.right!=null)
                q1.add(cur.right);
        }

    }
    /* static Node findLCA(Node root, Node n1, Node n2)
    {
        ArrayList<Integer> ar1 = new ArrayList<Integer>();
        ArrayList<Integer> ar2 = new ArrayList<Integer>();
        if(root==null)
            return null;
        

    } */
   public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of element you want to insert");
        int n = sc.nextInt();
        Node root=null;
        for(int i=0;i<n;i++)
        {
            root = insert(root,(sc.nextInt()));
        }
        System.out.println("Inorder Traverssal");
        inorder(root);
        System.out.println();
        System.out.println("Preorder Traverssal");
        preorder(root);
        System.out.println();
        System.out.println("Postorder Traverssal");
        postorder(root);
        System.out.println();
        System.out.println("Levelorder Traverssal");
        levelorder(root);
    }

}
